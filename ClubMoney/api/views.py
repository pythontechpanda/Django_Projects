from django.shortcuts import render,HttpResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from itertools import islice
from rest_framework.decorators import api_view
import firebase_admin
from firebase_admin import credentials, messaging


@api_view(['GET','POST'])
@csrf_exempt
def bslogin(request):
    if request.method =='GET':
        bs_regs = user_registration.objects.all()
        bs_ser = user_serializer(bs_regs, many=True)    
        return Response(bs_ser.data)
            
    if request.method =='POST':

        # token = Token.objects.create(mobileno=request.modileno)
        # print(token.key)    
        context= {}
        # mobileno = request.POST.get('mobileno')
        # password = request.POST.get('password')
        bs_ser = user_serializer(data=request.data)#data from ui
        mobile=request.data['mobileno']
        print(mobile)
        passw=request.data['password']
        print(passw)
        mydata = user_registration.objects.filter(mobileno=mobile,password=passw).values()
 
        if mydata:
            # try:
            #     bsre = user_registration.objects.get(id=id)
            #     print(bsre)
            # except user_registration.DoesNotExist:
            #     return Response(status=status.HTTP_404_NOT_FOUND)
            myid=mydata[0]
            print(myid['id'])
            context['response'] = 'Successfully Loged In'
            context['id'] = myid['id']
            context['mobileno'] = mobile
            context['status'] = 'True'
            return Response(context,status=status.HTTP_200_OK)

        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid Credential'
            context['status'] = 'False'
            return Response(context,status=status.HTTP_404_NOT_FOUND)
        
        
        

class UserCreation(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = user_registration.objects.all()
        serializer = user_serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = user_registration.objects.get(id=id)
            serializer = user_serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = user_serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
         
            # userid=user_registration.objects.get(id=t)
            # clubid=club.objects.get(id=c)
            
            tokens = [serializer.data['token']]
            name = serializer.data['full_name']
            uid = serializer.data['id']
            # Create a message
            message = messaging.MulticastMessage(
                
                notification=messaging.Notification(
                    title='Club Invitation',
                    body=f'Hello {name}! \n You are Registered with CoinClub.',
                    image= 'https://meetjob.techpanda.art/media/club/NicePng_chilli-png_6961635.png'
                ),
                # data={
                #     'invite': 'Yes',
                #     'userid': str(userid.id),
                #     'clubid': str(clubid.id),
                #     'clubname': str(clubid.clubname),
                #     'totalmember': str(clubid.clubmembers),
                #     'totalamount': str(clubid.clubamount),
                #     'perhead' : str(clubid.clubcontribution),
                    
                    
                # },
                
                tokens=tokens,
            )
            # Send the message
            response = messaging.send_multicast(message)
            print(message.notification.body)
            my_nitif = AppNotification(usernotification_id=uid,title=message.notification.title, body=message.notification.body, data=message.notification.image)
            my_nitif.save()
            # Render the response
            # return HttpResponse('notification.html', {'response': response.success_count})
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = user_registration.objects.get(pk=id)
        serializer = user_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = user_registration.objects.get(pk=id)
        serializer = user_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = user_registration.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})




# Send notification UserKYC

def userkyc_notification(*args):
    
    # print('aaaa',args[0]['clubname']/////)
    t=args[0]['registeruser']
    # print('ttttttt',t.data)
    # c=args[0]['mobile']
    userid=user_registration.objects.get(id=t)
    # kycid=userkyc.objects.get(id=c)
    
  
    # userid=user_registration.objects.get(id=t)
    
    tokens = [userid.token]
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='KYC Notification',
            body=f'Hello {str(userid.full_name)}! \n You are successfully registered.',
        ),
        # data={
        #     'invite': 'Yes',
        #     'userid': str(userid.id),
        #     'clubid': str(clubid.id),
        #     'clubname': str(clubid.clubname),
        #     'totalmember': str(clubid.clubmembers),
        #     'totalamount': str(clubid.clubamount),
        #     'perhead' : str(clubid.clubcontribution),
            
            
        # },
        
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)
    # Render the response
    return HttpResponse('notification.html', {'response': response.success_count})






class userkycview(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = userkyc.objects.all()
        serializer = userkyc_serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = userkyc.objects.get(id=id)
            serializer = userkyc_serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = userkyc_serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            userkyc_notification(request.data)
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = userkyc.objects.get(pk=id)
        serializer = userkyc_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = userkyc.objects.get(pk=id)
        serializer = userkyc_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = userkyc.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})



class bankdetailview(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = bankdetail.objects.all()
        serializer = bank_serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = bankdetail.objects.get(id=id)
            serializer = bank_serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = bank_serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = bankdetail.objects.get(pk=id)
        serializer = bank_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = bankdetail.objects.get(pk=id)
        serializer = bank_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = bankdetail.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    

@api_view(['GET','POST'])
@csrf_exempt
def clubview(request):

    if request.method =='GET':
        bs_regs = club.objects.all()
        bs_ser = club_serializer(bs_regs, many=True)  
        return Response(bs_ser.data)
            
    if request.method =='POST':
        round_list=[]
        bs_ser = club_serializer(data=request.data)
        print(request.data['clubmembers'])
        batch=request.data['clubmembers']
        
        if bs_ser.is_valid(): 
            print("API Calling........")
            bs_ser.save()
            print(request.data['clubmembers'])
            batch_no=request.data['clubmembers']
            batch_name=request.data['clubname']
            # batch_id=request.data['id']
            print(bs_ser.data)
            objs = (rounds(roundname=batch_name+' round %s' % i, roundno=i, clubname=batch_name) for i in range(1,int(batch_no)+1))
            while True:
                batch = list(islice(objs, int(batch_no)))
                if not batch:
                    break
                print(type(batch))
                print(type(batch_no))
                round_list.append(batch)
                rounds.objects.bulk_create(batch, int(batch_no))
            print(round_list)
            return Response(bs_ser.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def clubviewupdate(request,id, format=None):
    try:
        bsre = club.objects.get(id=id)
    except club.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
         bs_ser = club_serializer(bsre)
         
         print(bs_ser)
         print(bs_ser['clubname'])
         batch=bs_ser['clubname'].value
         print(batch)
         r=rounds.objects.filter(clubname=batch)
         print(r)
         bs_ser_rounds = club_serializer1(r)
         print(bs_ser_rounds.data)
         return Response(bs_ser_rounds.data)
    elif request.method == 'PUT':
         bs_ser = club_serializer(bsre, data = request.data)
         if bs_ser.is_valid():
            bs_ser.save()
            return Response(bs_ser.data)
         return Response(bs_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bsre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
class roundview(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = rounds.objects.all()
        serializer = round_serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)
 
    # def retrieve(self, request, pk=None):
    #     id = pk
    #     if id is not None:
    #         stu = rounds.objects.get(id=id)
    #         serializer = round_serializer(stu)
    #         return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # club = name
        # id = pk
        if club is not None:
            stu = rounds.objects.filter(clubname=club)
            serializer = round_serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = round_serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = rounds.objects.get(pk=id)
        serializer = round_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = rounds.objects.get(pk=id)
        serializer = round_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = rounds.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    



class clubinvite(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = invite_user.objects.all()
        serializer = inviteuser_serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        # id = pk
        # if id is not None:
        #     stu = invite_user.objects.get(id=id)
        #     serializer = inviteuser_serializer(stu)
        #     return Response(serializer.data)
        id = pk
        if id is not None:
            # stu = invite_user.objects.get(id=id)
            stu = user_registration.objects.get(id=id)
            print(stu)
            inv = invite_user.objects.filter(inviteto=stu)
            print(inv)
            serializer = inviteuser_serializer(inv)
            print('this',serializer.data)
            return Response(serializer.data)

    def create(self, request):
        serializer = inviteuser_serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            
            clubinvite_notification(request.data)
            # clubinvite_notification(t,clubid.clubname,clubid.clubmembers,clubid.clubamount,clubid.clubcontribution)
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = invite_user.objects.get(pk=id)
        serializer = inviteuser_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = invite_user.objects.get(pk=id)
        serializer = inviteuser_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = invite_user.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})

def clubinvite_notification(*args):
    print('aaaa',args[0]['clubname'])
    t=args[0]['inviteto']
    # print('ttttttt',t.data)
    c=args[0]['clubname']
    userid=user_registration.objects.get(id=t)
    clubid=club.objects.get(id=c)
    
    # print(type(args[1]))
    # print(type(args[2]))
    # print(type(args[3]))
    tokens = [userid.token]
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='Club Invitation',
            body=f'Hello {str(userid.full_name)}! \n You are invited to join {str(clubid.clubname)} Club.',
            image= 'https://meetjob.techpanda.art/media/club/NicePng_chilli-png_6961635.png'
        ),
        data={
            'invite': 'Yes',
            'userid': str(userid.id),
            'clubid': str(clubid.id),
            'clubname': str(clubid.clubname),
            'totalmember': str(clubid.clubmembers),
            'totalamount': str(clubid.clubamount),
            'perhead' : str(clubid.clubcontribution),
            
            
        },
        
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)
    # Render the response
    return HttpResponse('notification.html', {'response': response.success_count})




class CustomerCareView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = CustomerCare.objects.all()
        serializer = CustomerCare_serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = CustomerCare.objects.get(id=id)
            serializer = CustomerCare_serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = CustomerCare_serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = CustomerCare.objects.get(pk=id)
        serializer = CustomerCare_serializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = CustomerCare.objects.get(pk=id)
        serializer = CustomerCare_serializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = CustomerCare.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    



class Issue_messages(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = IssueMessages.objects.all()
        serializer = Issue_messages_Serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = IssueMessages.objects.get(id=id)
            serializer = Issue_messages_Serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = Issue_messages_Serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created', 'issueresult':serializer.data}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentionView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = IssueMessages.objects.all()
        serializer = Issue_messages_Serializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = IssueMessages.objects.get(id=id)
            serializer = Issue_messages_Serializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = Issue_messages_Serializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created', 'issueresult':serializer.data}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# @api_view(['GET','POST'])
# def clubinvite(request):
#     if request.method =='GET':
#         bs_regs = invite_user.objects.all()
#         bs_ser = inviteuser_serializer(bs_regs, many=True)
#         return Response(bs_ser.data)
#     if request.method =='POST':
#         bs_ser = inviteuser_serializer(data=request.data)
#         if bs_ser.is_valid():
#             bs_ser.save()
#             return Response(bs_ser.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def userclub(request, pk=None):
    id = pk

    prod = user_registration.objects.get(id=pk)
    print('prod:',prod)
    menuf=invite_user.objects.filter(inviteto=prod)
    print('prod',menuf)
    
    d={}
    l=[]
    l1=[]
    totalam = 0
    for j in range(len(menuf)):
        d1={}
        # print('menuf[j]',type(menuf[j]))
        clubid=club.objects.get(clubname=str(menuf[j].clubname))
        d1.update({'club':str(menuf[j].clubname)})
        d1.update({'clubid':clubid.id})
        # d.update({'clubuser':l})
        d1.update({'clubname':str(clubid.clubname)})
        d1.update({'clubimage':str(clubid.clubimage)})
        d1.update({'clubamount':str(clubid.clubamount)})
        d1.update({'clubmembers':str(clubid.clubmembers)})
        d1.update({'clubcontribution':str(clubid.clubcontribution)})
        d1.update({'startdate':str(clubid.startdate)})
        d1.update({'starttime':str(clubid.starttime)})
        d1.update({'duration':str(clubid.duration)})
        d1.update({'is_completed':str(clubid.is_completed)})
        # d.update({'clubid':str(clubid.id)})
        print(d1)
        
        l.append(d1)
       
        
        totalam =totalam+int(clubid.clubamount)
    print("my amount",totalam)
    print('l',l)
    d.update({'user':str(prod)})
    d.update({'userclub':l})
    d.update({'userid':str(prod.id)})
    d.update({'usermobileno':prod.mobileno})
    d.update({'usercity':prod.city})
    d.update({'useroccupation':prod.occupation})
    d.update({'usermotive':prod.motive})
    d.update({'userincome':prod.income})
    d.update({'userwallet_amount':prod.wallet_amount})
    d.update({'usermonthlycontribution':prod.monthlycontribution})
    d.update({'userprofileimg':str(prod.profileimg)})
    d.update({'useremail':prod.email})
    d.update({'useralternateno':prod.alternateno})
    d.update({'usercreate_at':prod.create_at})
    d.update({'total_subscription':totalam})
    l1.append(d)
    # print(d)
    result=userclubSerializer(l1,many=True).data
    return Response(result)
        
        

@api_view(['GET'])
def clubuser(request, pk):
    id = pk


    prod = club.objects.get(id=pk)
    print('prod:',prod)
    menuf=invite_user.objects.filter(clubname=prod)
    print('prod',menuf)
    d={}
    l=[]
    l1=[]
        # print('menuf[j]',type(menuf[j]))
    
    for j in range(len(menuf)):
        d1={}
        print('menuf[j]',menuf[j])
        userid=user_registration.objects.get(full_name=str(menuf[j].inviteto))
        d1.update({'user':str(menuf[j].inviteto)})

        d1.update({'userid':userid.id})
        d1.update({'usermobileno':userid.mobileno})
        d1.update({'usercity':userid.city})
        d1.update({'useroccupation':userid.occupation})
        d1.update({'usermotive':userid.motive})
        d1.update({'userincome':userid.income})
        d1.update({'userwallet_amount':userid.wallet_amount})
        d1.update({'usermonthlycontribution':userid.monthlycontribution})
        d1.update({'userprofileimg':str(userid.profileimg)})
        d1.update({'useremail':userid.email})
        d1.update({'useralternateno':userid.alternateno})
        d1.update({'usercreate_at':userid.create_at})
        # print(d1)
        l.append(d1)
    print('l',l)
    d.update({'club':str(prod)})
    d.update({'clubuser':l})
    d.update({'clubname':str(prod.clubname)})
    d.update({'clubimage':str(prod.clubimage)})
    d.update({'clubamount':str(prod.clubamount)})
    d.update({'clubmembers':str(prod.clubmembers)})
    d.update({'clubcontribution':str(prod.clubcontribution)})
    d.update({'startdate':str(prod.startdate)})
    d.update({'starttime':str(prod.starttime)})
    d.update({'duration':str(prod.duration)})
    d.update({'is_completed':str(prod.is_completed)})
    l1.append(d)
    # print(d)
    result=clubuserSerializer(l1,many=True).data
    return Response(result)

@api_view(['GET'])
def clubroundsfilter(request, pk=None):
    id = pk

    prod = club.objects.get(id=pk)
    print('prod:',prod)
    menuf=invite_user.objects.filter(clubname=prod)
    print('prod',menuf)
    
    l=[]
    for j in range(len(menuf)):
        # print('menuf[j]',type(menuf[j]))
        l.append(str(menuf[j].inviteto))
    print('l',l)
    # d.update({str(prod[i]):l})
    # print(d)
    return Response({str(prod):l})


@api_view(['GET'])
def clubuser(request, pk):
    id = pk


    prod = club.objects.get(id=pk)
    print('prod:',prod)
    menuf=invite_user.objects.filter(clubname=prod)
    print('prod',menuf)
    d={}
    l=[]
    l1=[]
        # print('menuf[j]',type(menuf[j]))
    
    for j in range(len(menuf)):
        d1={}
        print('menuf[j]',menuf[j])
        userid=user_registration.objects.get(full_name=str(menuf[j].inviteto))
        d1.update({'user':str(menuf[j].inviteto)})
        d1.update({'userid':userid.id})
        d1.update({'usermobileno':userid.mobileno})
        d1.update({'usercity':userid.city})
        d1.update({'useroccupation':userid.occupation})
        d1.update({'usermotive':userid.motive})
        d1.update({'userincome':userid.income})
        d1.update({'userwallet_amount':userid.wallet_amount})
        d1.update({'usermonthlycontribution':userid.monthlycontribution})
        d1.update({'userprofileimg':str(userid.profileimg)})
        d1.update({'useremail':userid.email})
        d1.update({'useralternateno':userid.alternateno})
        d1.update({'usercreate_at':userid.create_at})
        print(d1)
        l.append(d1)
    print('l',l)
    d.update({'club':str(prod)})
    d.update({'clubuser':l})
    d.update({'clubname':str(prod.clubname)})
    d.update({'clubimage':str(prod.clubimage)})
    d.update({'clubamount':str(prod.clubamount)})
    d.update({'clubmembers':str(prod.clubmembers)})
    d.update({'clubcontribution':str(prod.clubcontribution)})
    d.update({'startdate':str(prod.startdate)})
    d.update({'starttime':str(prod.starttime)})
    d.update({'duration':str(prod.duration)})
    d.update({'is_completed':str(prod.is_completed)})
    d.update({'clubid':str(prod.id)})
    l1.append(d)
    # print(d)
    result=clubuserSerializer(l1,many=True).data
    return Response(result)



class AddMoneyView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = AddMoney.objects.all()
        serializer = AddMoneySerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = AddMoney.objects.get(id=id)
            serializer = AddMoneySerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = AddMoneySerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Amount Added Successfull.'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        stu = AddMoney.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})





class WithdrawAmountView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = WithdrawMoney.objects.all()
        serializer = WithdrawMoneySerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = WithdrawMoney.objects.get(id=id)
            serializer = WithdrawMoneySerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = WithdrawMoneySerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Amount Withdraw Successfull.'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        stu = WithdrawMoney.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})







class AvgTrasferTimeView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = AvgTrasferTime.objects.all()
        serializer = AvgTrasferTimeSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = AvgTrasferTime.objects.get(id=id)
            serializer = AvgTrasferTimeSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = AvgTrasferTimeSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Amount Withdraw Successfull.'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        stu = AvgTrasferTime.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
    
    
class AmountTrasferTimeView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = AmountTrasferTime.objects.all()
        serializer = AmountTrasferTimeSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = AmountTrasferTime.objects.get(id=id)
            serializer = AmountTrasferTimeSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = AmountTrasferTimeSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Amount Transfered Successfull.'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        stu = AmountTrasferTime.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    




class ClubClosedTimeView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = ClubClosedTime.objects.all()
        serializer = ClubClosedTimeSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = ClubClosedTime.objects.get(id=id)
            serializer = ClubClosedTimeSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = ClubClosedTimeSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'club closed Successfull.'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id = pk
        stu = ClubClosedTime.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    

# class GetClubByUserView(viewsets.ViewSet):
#     def list(self, request):      # list - get all record
#         stu = GetClubByUser.objects.all()
#         serializer = GetClubByUserSerializer(stu, many=True)    # many use for bulk data come 
#         return Response(serializer.data)


#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = GetClubByUser.objects.get(id=id)
#             serializer = GetClubByUserSerializer(stu)
#             return Response(serializer.data)

   


class GetBidData(viewsets.ViewSet):
    pass
    # def list(self, request):      # list - get all record
    #     stu = .objects.all()
    #     serializer = Issue_messages_Serializer(stu, many=True)    # many use for bulk data come 
    #     return Response(serializer.data)


    # def retrieve(self, request, pk=None):
    #     id = pk
    #     if id is not None:
    #         stu = IssueMessages.objects.get(id=id)
    #         serializer = Issue_messages_Serializer(stu)
    #         return Response(serializer.data)

    # def create(self, request):
    #     serializer = Issue_messages_Serializer(data = request.data)  # form data conviert in json data
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Created', 'issueresult':serializer.data}, status= status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from datetime import datetime, timedelta

from firebase_admin import messaging

def send_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        token=token,
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


def my_view(request):
    # Create a time list
    times = [datetime.now() + timedelta(minutes=i) for i in range(5)]

    # Loop through the time list and send notifications
    for time in times:
        if datetime.now() == time:
            send_notification("dyJDr1HVR7SJyj7ZBcaTEb:APA91bHRQfvLSBxHW_1wbME4J5g-ZiLM_GXDZmAleocQMhQGg6nGyO28r5pa7WdH7m38FZE8AJp1n2tWhltOmlCVCD33ucc7v1QnUMUxpyM9rUvcRhhA57tJRp8NbiUFkKP5ayV5bkpu",
                          "Notification Title", "Notification Body")
            print(time)
        else:
            continue

    return HttpResponse("Notifications sent!")



class AppNotificationView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = AppNotification.objects.all()
        serializer = AppNotificationSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = AmountTrasferTime.objects.get(id=id)
            serializer = AppNotificationSerializer(stu)
            return Response(serializer.data)

    

    def destroy(self, request, pk):
        id = pk
        stu = AppNotification.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
@api_view(['GET'])
def paymentremainder(request, pk):
    winner=paymentrecord.objects.filter(winner=pk, is_paid=False)
    for i in winner:
        print(i.looser)
        print(i.winner)
        lossertoken=user_registration.objects.get(id=i.looser.id)
        tokens = [str(lossertoken.token)]
        # tokens= ['dyJDr1HVR7SJyj7ZBcaTEb:APA91bHRQfvLSBxHW_1wbME4J5g-ZiLM_GXDZmAleocQMhQGg6nGyO28r5pa7WdH7m38FZE8AJp1n2tWhltOmlCVCD33ucc7v1QnUMUxpyM9rUvcRhhA57tJRp8NbiUFkKP5ayV5bkpu']
        message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title='Payment Remainder',
            body=f'Hello {str(i.looser)}! \n{str(i.winner)} is the winner of {str(i.roundpayment)}. You have to pay them within 24hrs., otherwise you have to pay panlties.',
            image= 'https://meetjob.techpanda.art/media/club/NicePng_chilli-png_6961635.png'
        ),
        # data={
        #     'invite': 'Yes',
        #     'userid': str(userid.id),
        #     'clubid': str(clubid.id),
        #     'clubname': str(clubid.clubname),
        #     'totalmember': str(clubid.clubmembers),
        #     'totalamount': str(clubid.clubamount),
        #     'perhead' : str(clubid.clubcontribution),
        # },
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)
    print(message.notification.body)
    my_nitif = AppNotification(usernotification_id=uid,title=message.notification.title, body=message.notification.body, data=message.notification.image)
    my_nitif.save()
    print(winner)
    return Response({'winner':'sent'})