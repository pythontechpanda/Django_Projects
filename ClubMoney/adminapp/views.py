from django.shortcuts import render,redirect,HttpResponse
from api.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from pusher_push_notifications import PushNotifications
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, messaging
from datetime import datetime



def SignUp(request):
    if request.method == 'POST':
        name = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pwd']
        date = datetime.now()
        
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('/')
        else:
            uobj = User(first_name=name, last_name=lname, email=email, username=username, password=make_password(password), is_superuser=True, date_joined=date)
            uobj.save()
            data= uobj.first_name
            messages.success(request, f"{data} Your Account Has Been Created!")
            return redirect('/')
    else:
        return render(request, 'signup.html')


def login_sys(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        print(uname)
        user = authenticate(username=uname, password=pwd)
        # print(user.date_joined)

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/homepage/')
            # elif user.is_staff:                                 # Admin
            #     return redirect('/admins/')
            # elif user.is_manager:
            #     return redirect('/leadadmin/')
            
        else:
            return redirect('/')
    
    return render(request, "login.html")
	

def logout_call(request):
	logout(request)
	return redirect('/login/')




# Create your views here.
def IndexPage(request):
    userget = user_registration.objects.all().count()
    allclub = club.objects.all().count()
    allrounds = rounds.objects.all().count()
    context = {
        'user': userget,
        'club': allclub,
        'allrounds' : allrounds,
    }
    return render(request, "index.html", context)

def UserTableData(request):
    getUser = user_registration.objects.all()
    return render(request, "tables-general.html", {'users':getUser})

def UserKycPage(request):
    getKyc = userkyc.objects.all()
    return render(request, "userkyc.html", {'kyc':getKyc})

def ClubPage(request):
    getClub = club.objects.all()
    return render(request, "club.html", {'clubs':getClub})

def RoundsPage(request):
    getRound = rounds.objects.all()
    return render(request, "rounds.html", {'rounds':getRound})

def IssuePage(request):
    getIssue = IssueMessages.objects.all()
    return render(request, "issues.html", {'issues':getIssue})

def CustomerCarePage(request):
    getService = CustomerCare.objects.all()
    return render(request, "customercare.html", {'services':getService})

def InvitePage(request):
    getInvite = invite_user.objects.all()
    return render(request, "inviteto.html", {'invites':getInvite})

def CashWalletPage(request):
    getCashe = cashwallet.objects.all()
    return render(request, "wallet.html", {'wallet':getCashe})

def AppNotificationPage(request):
    getNotif = AppNotification.objects.all()
    return render(request, "notifications.html", {'notifi':getNotif})


def AppNotificationPage(request):
    getNotif = AppNotification.objects.all()
    return render(request, "notifications.html", {'notifi':getNotif})

def PaymentrecordPage(request):
    getPay = paymentrecord.objects.all()
    return render(request, "payment.html", {'payment':getPay})

#--------------------
def WithdrawMoneyPage(request):
    getWithdraw = WithdrawMoney.objects.all()
    return render(request, "withdraw.html", {'withdraw':getWithdraw})


def GetClubByUserPage(request):
    clubbyuser = GetClubByUser.objects.all()
    return render(request, "clubbyuser.html", {'getclub':clubbyuser})

def ClubClosedTimePage(request):
    clubclose = ClubClosedTime.objects.all()
    return render(request, "clubclosetime.html", {'getclose':clubclose})
def AvgTrasferTimePage(request):
    avg = AvgTrasferTime.objects.all()
    return render(request, "avgtransfertime.html", {'getavgtrans':avg})

def AmountTrasferTimePage(request):
    amt = AmountTrasferTime.objects.all()
    return render(request, "amountransfertime.html", {'getamttrans':amt})

def BankDetailPage(request):
    getBank = bankdetail.objects.all()
    return render(request, "bankdetail.html", {'banks':getBank})

def CustomerCarePage(request):
    getCustmer = CustomerCare.objects.all()
    return render(request, "customercare.html", {'Custmercare':getCustmer})

def createUser(request):
    if request.method == 'POST':
        fnm = request.POST['full_name']
        mnm = request.POST['mobileno']
        lnm = request.POST['city']
        gen = request.POST['gender']
        dob = request.POST['occupation']
        email = request.POST['motive']
        contact = request.POST['income']
        alt_contact = request.POST['monthlycontribution']
        profileimg = request.FILES['profileimg']
        email = request.POST['email']
        alternateno = request.POST['alternateno']
        

        if user_registration.objects.filter(email=email).exists():
                messages.info(request, 'Username is already taken')
                return redirect('/homepage/createnewuser/')
        else:
            ulead = user_registration(full_name=fnm,
                            mobileno=mnm,
                            city=lnm,
                            gender=gen,
                            occupation=dob,
                            motive=email,
                            income=contact,
                            monthlycontribution=alt_contact,
                            profileimg=profileimg,
                            email=email,
                            alternateno=alternateno,)
            ulead.save()
            messages.success(request, "Account has been created successfully")
            return redirect('/homepage/createnewuser/')
    
    else:
        return render(request, "createuser.html")


def UpdateUser(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        fnm = request.POST['full_name']
        mnm = request.POST['mobileno']
        lnm = request.POST['city']
        gen = request.POST['gender']
        dob = request.POST['occupation']
        email = request.POST['motive']
        contact = request.POST['income']
        alt_contact = request.POST['monthlycontribution']
        # profileimg = request.POST['address']
        email = request.POST['email']
        alternateno = request.POST['alternateno']
        
        # led_id = LeadCreate.objects.get(id=id)
        
        uplead = user_registration.objects.filter(id=id)
        
        uplead.update(full_name=fnm,
                            mobileno=mnm,
                            city=lnm,
                            gender=gen,
                            occupation=dob,
                            motive=email,
                            income=contact,
                            monthlycontribution=alt_contact,
                            # profileimg=address,
                            email=email,
                            alternateno=alternateno,
                           )
        messages.success(request, f"{fnm}, profile updated successfully")
        # return redirect('/superadmin/edit_leadinfo//')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  
    else:
        getUser = user_registration.objects.get(id=id)    
        return render(request, "edituser.html", {'user':getUser})
    # return render(request, "edituser.html")
    


def DeleteUser(request, id):
    data = user_registration.objects.get(id=id)
    data.delete()
    messages.success(request, f"{data.full_name}, has been deleted succsessfull")
    return redirect('/homepage/getalluser/')



def CreateClub(request):
    if request.method == 'POST':
        clubname = request.POST['clubname']
        clubimage = request.FILES['clubimage']
        clubamount = request.POST['clubamount']
        clubmembers = request.POST['clubmembers']
        clubcontribution = request.POST['clubcontribution']
        # startdate = request.POST['startdate']
        # starttime = request.POST['starttime']
        # duration = request.POST['duration']
        if club.objects.filter(clubname=clubname).exists():
                messages.info(request, 'Club name is already taken')
                return redirect('/homepage/createclub/')
        else:
            newclub = club(clubname=clubname,
                        clubamount=clubamount,
                        clubmembers=clubmembers,
                        clubcontribution=clubcontribution,
                        clubimage=clubimage
                        )
            newclub.save()
            
        # bs_ser = club.objects.all()
     
        print(request.POST['clubmembers'])
        batch_no=request.POST['clubmembers']
        batch_name=request.POST['clubname']
        # batch_id=request.data['id']
        # print(bs_ser.data)
        
        round_list=[]
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
        messages.success(request, "Club has been created successfully")
        return redirect('/homepage/createclub/')
    
    else:
        return render(request, "clubcreate.html")





def UpdateClub(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        clubname = request.POST['clubname']
        # clubimage = request.POST['clubimage']
        clubamount = request.POST['clubamount']
        clubmembers = request.POST['clubmembers']
        clubcontribution = request.POST['clubcontribution']
        # startdate = request.POST['startdate']
        # starttime = request.POST['starttime']
        # duration = request.POST['duration']
        
        uplead = club.objects.filter(id=id)
        
        uplead.update(
                        clubname=clubname,
                        clubamount=clubamount,
                        clubmembers=clubmembers,
                        clubcontribution=clubcontribution,
                        # startdate=startdate,
                        # starttime=starttime,
                        # duration=duration
                        
                        )
        messages.success(request, f"{clubname} club detail updated successfully")
        return redirect('/homepage/getallclub/')
        # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        myclub = club.objects.get(id=id)    
        return render(request, "editclub.html", {'myclub':myclub})
    # return render(request, "edituser.html")



def DetailClub(request, id):
       myclub = club.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'myclub':myclub, 'adduser':getUser})
   
   
   
def DeleteClub(request, id):
    data = club.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getallclub/')




# def inviteUser(*args):
#     # print('aaaa',args[0]['clubname'])
#     # t=args[0]['inviteto']
#     # # print('ttttttt',t.data)
#     # c=args[0]['clubname']
#     userid=user_registration.objects.get(id=args[0])
#     clubid=club.objects.get(id=args[0])
    
#     # print(type(args[1]))
#     # print(type(args[2]))
#     # print(type(args[3]))
#     tokens = [userid.token]
#     # Create a message
#     message = messaging.MulticastMessage(
        
#         notification=messaging.Notification(
#             title='Club Invitation',
#             body='This is a Notification to Join Techpanda Club.',
#             image= 'https://meetjob.techpanda.art/media/club/NicePng_chilli-png_6961635.png'
#         ),
#         data={
#             'invite': 'Yes',
#             'userid': str(userid.id),
#             'clubid': str(clubid.id),
#             'clubname': str(clubid.clubname),
#             'totalmember': str(clubid.clubmembers),
#             'totalamount': str(clubid.clubamount),
#             'perhead' : str(clubid.clubcontribution),
            
            
#         },
        
#         tokens=tokens,
#     )
#     # Send the message
#     response = messaging.send_multicast(message)
#     # Render the response
#     return render( 'notification.html', {'response': response.success_count})



# def inviteUser(request, id, uid):
#     getUser = user_registration.objects.get(id=id)
#     myclub = club.objects.get(id=uid)
#     # print(getUser.id, myclub.id)
#     push_notify(getUser.id, myclub.id)
#     return render(request, "test.html", {'myclub':myclub, 'adduser':getUser})
#     # return render(request, 'club.html')


def UserVerification(request, id):
    userid = user_registration.objects.get(id=id)
    # clubid = userkyc.objects.get(id=uid)
    tokens = [userid.token]
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='KYC Status',
            body=f'Hello {str(userid.full_name)}!\n Your KYC is Aproved.',
            # image= 'asasd'
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
    my_nitif = AppNotification(usernotification=userid,title=message.notification.title, body=message.notification.body)
    my_nitif.save()
    # return HttpResponse(request,'hi')
    # messages.success(request, "Club Invitation send successfully")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    


def UserVerificationReject(request, id):
    userid = user_registration.objects.get(id=id)
    # clubid = userkyc.objects.get(id=uid)
    tokens = [userid.token]
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='KYC Invitation',
            body=f'Hello {str(userid.full_name)}!\n Your KYC is Rejected.',
            # image= 'asasd'
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
    my_nitif = AppNotification(usernotification=userid,title=message.notification.title, body=message.notification.body)
    my_nitif.save()
    # return HttpResponse(request,'hi')
    # messages.success(request, "Club Invitation send successfully")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    

def inviteUser(request, id, uid):
    userid = user_registration.objects.get(id=id)
    clubid = club.objects.get(id=uid)
    tokens = [userid.token]
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='Club Invitation',
            body=f'Hello {str(userid.full_name)}!\n You are invited to join {str(clubid.clubname)} Club.',
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
    my_nitif = AppNotification(usernotification=userid,title=message.notification.title, body=message.notification.body, image=message.notification.image)
    my_nitif.save()
    messages.success(request, "Club Invitation send successfully")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    # print(getUser.id, myclub.id)
    # push_notify(getUser.id, myclub.id)
    # return render(request, "test.html", {'myclub':clubid, 'adduser':userid})
    # return render(request, 'club.html')

def push_notify(*args):
    print("serrrrrrrrrrrr",args[0])
    getUser = user_registration.objects.get(id=args[0])
    mycl = club.objects.get(id=args[1])
    print(args)
    print(getUser)
    # for i in myclub:
    #     print(i.id)
    #  ({'id': 8, 'full_name': 'Pragati Sharma', 'mobileno': '998889987821', 'city': 'Banglore',
    #   'password': '12345', 'gender': 'female', 'occupation': 'Software Engeenier', 'motive': 'saving',
    #    'income': '30000', 'monthlycontribution': '3000',
    #   'profileimg': None, 'email': 'pragati@gmail.com',
    #    'alternateno': '009899099921', 'create_at': '2023-02-21'}, 1)
    beams_client = PushNotifications(
        instance_id='53566661-977b-4140-b02f-cfbdb4b591a0',
        secret_key='F684617CEB1256469383278464FEDD07A9F5E9C0ABF83FEFBD9D06DCAC1254CE',
    )
    response = beams_client.publish_to_interests(
    interests=['hello'],
    publish_body={
            'apns': {
                'aps': {
                    'alert': 'Hello python!'
                }
            },
            'fcm': {
                'notification': {
                    'title': 'Hello python',
                    'body': 'Hello, '+str(getUser)+'!' +'\nYou are Invited to join '+str(mycl)+'.'
                },
                'data': {
                    'sender': 'Python',
                    'message': 'Hello, '+str(getUser)+'!' +'\nYou are Invited to join '+str(mycl)+'.'
                },
                "to":"device token"
            }
        }
    )
    print(response['publishId'])
    # response = beams_client.publish_to_users(
    #     user_ids=[str(args[0])],
    #     publish_body={
    #         'apns': {
    #             'aps': {
    #                 'alert': 'Hello!'
    #             }
    #         },
    #         'fcm': {
    #             'notification': {
    #                 'title': 'Hello',
    #                 'body': 'Hello, python hu me aapka!'
    #             }
    #         }
    #     }
    # )
    # print(response['publishId'])
    
    

def UpdateRounds(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        clubname = request.POST['clubname']
        roundno = request.POST['roundno']
        roundname = request.POST['roundname']
        minbid = request.POST['minbid']
        maxbid = request.POST['maxbid']
        winner = request.POST['winner']
        roundamount = request.POST['roundamount']
        status = request.POST['status']
        starttime = request.POST['starttime']
        startdate = request.POST['startdate']
        duration = request.POST['duration']
        # is_completed = request.POST['is_completed']
        
        # led_id = LeadCreate.objects.get(id=id)
        
        uplead = rounds.objects.filter(id=id)
        
        uplead.update(clubname=clubname,
                            roundno=roundno,
                            roundname=roundname,
                            minbid=minbid,
                            maxbid=maxbid,
                            winner=winner,
                            roundamount=roundamount,
                            status=status,
                            starttime=starttime,
                            startdate=startdate,
                            duration=duration,
                            is_completed=False
                           )
        messages.success(request, f"{clubname}, round updated successfully")
        # return redirect('/superadmin/edit_leadinfo//')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  
    else:
        getRound = rounds.objects.get(id=id)    
        return render(request, "editround.html", {'round':getRound})
    # return render(request, "edituser.html")
    


def DeleteRound(request, id):
    data = rounds.objects.get(id=id)
    data.delete()
    messages.success(request, f"{data.full_name}, has been deleted succsessfull")
    return redirect('/homepage/getalluser/')



def CreateIssue(request):
    if request.method == 'POST':
        message = request.POST['message']
        
        if IssueMessages.objects.filter(message=message).exists():
                messages.info(request, 'Message is already taken')
                return redirect('/homepage/getallissue/')
        else:
            newclub = IssueMessages(message=message)
            newclub.save()

        return redirect('/homepage/getallissue/')
    
    else:
        return render(request, "createissue.html")


def UpdateIssue(request, id):
    if request.method == 'POST':
        issue = request.POST['message']
        
        uplead = IssueMessages.objects.filter(id=id)
        
        uplead.update(message=issue)
        messages.success(request, f"{issue}, message updated successfully")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  
    else:
        getIssue = IssueMessages.objects.get(id=id)    
        return render(request, "editissue.html", {'issue':getIssue})
    # return render(request, "edituser.html")
    


def DeleteIssue(request, id):
    data = IssueMessages.objects.get(id=id)
    data.delete()
    messages.success(request, f"{data.message}, has been deleted succsessfull")
    return redirect('/homepage/getallissue/')



def CreateInvite(request):
    
    if request.method == 'POST':
        clubname = request.POST['clubname']
        inviteto = request.POST['inviteto']
        is_join = request.POST['is_join']
        
        # if invite_user.objects.filter(clubname=clubname).exists():
        #         messages.info(request, 'Message is already taken')
        #         return redirect('/homepage/getallissue/')
        # else:
        newclub = invite_user(clubname_id=clubname,inviteto_id=inviteto,is_join=is_join)
        newclub.save()
        messages.success(request, "User invited successfully")
        return redirect('/homepage/createinvite/')
    
    else:
        getUser = user_registration.objects.all()
        getClub = club.objects.all()
        return render(request, "createinvite.html", {'user':getUser, 'club':getClub})


def UpdateInvite(request, id):
    if request.method == 'POST':
        clubname = request.POST['clubname']
        inviteto = request.POST['inviteto']
        is_join = request.POST['is_join']
        
        uplead = invite_user.objects.filter(id=id)
        
        uplead.update(clubname_id=clubname,inviteto_id=inviteto,is_join=is_join)
        messages.success(request, "Invite updated successfully")
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  
    else:
        getInvite = invite_user.objects.get(id=id)    
        getUser = user_registration.objects.all()
        getClub = club.objects.all()
        return render(request, "editinviteto.html", {'invite':getInvite,'user':getUser, 'club':getClub})
    # return render(request, "edituser.html")
    


def DeleteInvite(request, id):
    data = invite_user.objects.get(id=id)
    data.delete()
    messages.success(request, "Invite has been deleted succsessfull")
    return redirect('/homepage/getallissue/')





def CreateUserKyc(request):
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        address = request.POST['address']
        mobile = request.POST['mobile']
        fullname = request.POST['fullname']
        email = request.POST['email']
        aadharno = request.POST['aadharno']
        aadharfrontimg = request.FILES['aadharfrontimg']
        aadharbackimg = request.FILES['aadharbackimg']
        panno = request.POST['panno']
        panimg = request.FILES['panimg']
        is_verified = request.POST['is_verified']
        
        
        if userkyc.objects.filter(registeruser=registeruser).exists():
                messages.info(request, 'User Kyc is already taken')
                return redirect('/homepage/createkyc/')
        else:
            newclub = userkyc(registeruser_id=registeruser,
                        address=address,
                        mobile=mobile,
                        fullname=fullname,
                        email=email,
                        aadharno=aadharno,
                        aadharfrontimg=aadharfrontimg,
                        aadharbackimg=aadharbackimg,
                        panno=panno,
                        panimg=panimg,
                        is_verified=is_verified
                        )
            newclub.save()
            
        messages.success(request, "User Kyc has been created successfully")
        return redirect('/homepage/createkyc/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createuserkyc.html", {'users': user})





def UpdateUserKyc(request, id):
    # my_users = user_registration.objects.get(id=uid)
    # mykyc = userkyc.objects.get(id=id) 
    # print(my_users)
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        address = request.POST['address']
        mobile = request.POST['mobile']
        fullname = request.POST['fullname']
        email = request.POST['email']
        aadharno = request.POST['aadharno']
        # aadharfrontimg = request.FILES['aadharfrontimg']
        # aadharbackimg = request.FILES['aadharbackimg']
        panno = request.POST['panno']
        # panimg = request.FILES['panimg']
        is_verified = request.POST['is_verified']
        uplead = userkyc.objects.filter(id=id)
        uplead.update(registeruser_id=registeruser,
                        address=address,
                        mobile=mobile,
                        fullname=fullname,
                        email=email,
                        aadharno=aadharno,
                        # aadharfrontimg=aadharfrontimg,
                        # aadharbackimg=aadharbackimg,
                        panno=panno,
                        # panimg=panimg,
                        is_verified=is_verified
                        )
        # if is_verified == True:
        #     UserKycNotification()
        # else:
        #     print('pppppppppppppppppppp')
        messages.success(request, f"{registeruser} Kyc detail updated successfully")
        return redirect('/homepage/getallkyc/')
        # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mykyc = userkyc.objects.get(id=id)    
        user = user_registration.objects.all()
        return render(request, "edituserkyc.html", {'kyc':mykyc, 'users': user})
    # return render(request, "edituser.html")




# KYC Notification 


def UserKycNotification(request, kycid):
    # userid = user_registration.objects.get(id=id)
    # print(userid.full_name)
    kycid = userkyc.objects.get(id=kycid)
    print(kycid.registeruser)
    tokens = [kycid.registeruser.token]
    # print(userid)
    # Create a message
    message = messaging.MulticastMessage(
        
        notification=messaging.Notification(
            title='KYC Status',
            body=f'Hello {str(kycid.registeruser.full_name)}!\n You are KYC Process is completed.',
            # image= {str(userid.profileimg)}
        ),
        # data={
        #     'invite': 'Yes',
        #     'userid': str(userid.id),
        #     'clubid': str(clubid.id),
        #     'clubname': str(clubid.clubname),
        #     'totalmember': str(clubid.clubmembers),
        #     'totalamount': str(clubid.clubamount),
        #     'perhead' : str(clubid.clubcontribution), 
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)
    print(response)
    messages.success(request, "KYC Success")
    return redirect('/homepage/getallkyc/')
    # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))







def DetailUserKycView(request, id):
       mykyc = userkyc.objects.get(id=id)
    #    getUser = user_registration.objects.all()
    #    for i in getUser:
    #        print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail_kyc.html", {'mykyc':mykyc})
   
   
   
def DeleteUserKyc(request, id):
    data = userkyc.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getalluser/')





def CreateCashWallet(request):
    if request.method == 'POST':
        userwallet = request.POST['userwallet']
        walletamount = request.POST['walletamount']
        add_date = datetime.now()
        walletimg = request.FILES['walletimg']
        # walletwithdraw = request.POST['walletwithdraw']
        is_added = request.POST['is_added']
        # is_withdraw = request.POST['is_withdraw']
        

        newclub = cashwallet(userwallet_id=userwallet,
                             walletamount=walletamount,
                             casdate=add_date,
                             walletimg=walletimg,
                            #  walletwithdraw=walletwithdraw,
                             is_added=is_added,
                            #  is_withdraw=is_withdraw
                            )
        newclub.save()
    
        messages.success(request, "Wallet has been created successfully")
        return redirect('/homepage/createcashwallet/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createwallet.html", {'users': user})





def UpdateCashWallet(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        userwallet = request.POST['userwallet']
        walletamount = request.POST['walletamount']
        # totalamount = request.POST['totalamount']
        # walletimg = request.FILES['walletimg']
        # walletwithdraw = request.POST['walletwithdraw']
        is_added = request.POST['is_added']
        
        uplead = cashwallet.objects.filter(id=id)
        
        uplead.update(userwallet_id=userwallet,
                             walletamount=walletamount,
                            #  totalamount=totalamount,
                            #  walletimg=walletimg,
                            #  walletwithdraw=walletwithdraw,
                             is_added=is_added,
                        )
        messages.success(request, f"{walletamount} Add Cash updated successfully")
        return redirect('/homepage/getcashwallet/')
        # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = cashwallet.objects.get(id=id)    
        user = user_registration.objects.all()
        return render(request, "editwallet.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailCashWallet(request, id):
       myclub = userkyc.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'myclub':myclub, 'adduser':getUser})
   
   
   
def DeleteCashWallet(request, id):
    data = userkyc.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getcashwallet/')







def CreateCashWithdraw(request):
    if request.method == 'POST':
        userwallet = request.POST['userwallet']
        walletwithdraw = request.POST['walletwithdraw']
        add_date = datetime.now()
        payment_status = request.POST['payment_status']
        

        newclub = WithdrawMoney(userwallet_id=userwallet,
                             withdrawamount=walletwithdraw,
                             withdraw_date=add_date,
                             payment_status=payment_status,
                            )
        newclub.save()
    
        messages.success(request, "Withdraw request sent")
        return redirect('/homepage/withdrawamount/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createwithdraw.html", {'users': user})





def UpdateCashWithdraw(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        userwallet = request.POST['userwallet']
        walletwithdraw = request.POST['walletwithdraw']
        add_date = datetime.now()
        payment_status = request.POST['payment_status']
        
        uplead = WithdrawMoney.objects.filter(id=id)
        
        uplead.update(userwallet_id=userwallet,
                             withdrawamount=walletwithdraw,
                             withdraw_date=add_date,
                             payment_status=payment_status,
                        )
        messages.success(request, f"{walletwithdraw} Add Cash updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = WithdrawMoney.objects.get(id=id)    
        user = user_registration.objects.all()
        return render(request, "editwithdraw.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailCashWithdraw(request, id):
       mywithdraw = WithdrawMoney.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteCashWithdraw(request, id):
    data = WithdrawMoney.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getcashwithdraw/')




def CreateBankDetailView(request):
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        IFSCcode = request.POST['IFSCcode']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        passbookimg = request.FILES['passbookimg']
        registerno = request.POST['registerno']
        

        newclub = bankdetail(registeruser_id=registeruser,
                             IFSCcode=IFSCcode,
                             accountname=accountname,
                             accountnumber=accountnumber,
                             passbookimg=passbookimg,
                             registerno=registerno
                            )
        newclub.save()
    
        messages.success(request, "Bank Detail Created")
        return redirect('/homepage/createbankdetail/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createbankdetail.html", {'users': user})





def UpdateBankDetail(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        IFSCcode = request.POST['IFSCcode']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        # passbookimg = request.FILES['passbookimg']
        
        uplead = bankdetail.objects.filter(id=id)
        
        uplead.update(registeruser_id=registeruser,
                             IFSCcode=IFSCcode,
                             accountname=accountname,
                             accountnumber=accountnumber,
                            #  passbookimg=passbookimg
                        )
        messages.success(request, f"{accountname}, Bank details updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = bankdetail.objects.get(id=id)    
        user = user_registration.objects.all()
        return render(request, "editbankdetail.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailBankDetail(request, id):
       mywithdraw = bankdetail.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteBankDetail(request, id):
    data = bankdetail.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull") sorry na yr me wait kar raha hu kabse baat krne ke liye
    return redirect('/homepage/getallbanks/')





def CreateBankDetailView(request):
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        IFSCcode = request.POST['IFSCcode']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        passbookimg = request.FILES['passbookimg']
        registerno = request.POST['registerno']
        

        newclub = bankdetail(registeruser_id=registeruser,
                             IFSCcode=IFSCcode,
                             accountname=accountname,
                             accountnumber=accountnumber,
                             passbookimg=passbookimg,
                             registerno=registerno
                            )
        newclub.save()
    
        messages.success(request, "Bank Detail Created")
        return redirect('/homepage/createbankdetail/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createbankdetail.html", {'users': user})



def UpdateBankDetail(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        IFSCcode = request.POST['IFSCcode']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        # passbookimg = request.FILES['passbookimg']
        
        uplead = bankdetail.objects.filter(id=id)
        
        uplead.update(registeruser_id=registeruser,
                             IFSCcode=IFSCcode,
                             accountname=accountname,
                             accountnumber=accountnumber,
                            #  passbookimg=passbookimg
                        )
        messages.success(request, f"{accountname}, Bank details updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = bankdetail.objects.get(id=id)    
        user = user_registration.objects.all()
        return render(request, "editbankdetail.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailBankDetail(request, id):
       mywithdraw = bankdetail.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteBankDetail(request, id):
    data = bankdetail.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull") 
    return redirect('/homepage/getallbanks/')




def CustomerCareView(request):
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        IFSCcode = request.POST['IFSCcode']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        passbookimg = request.FILES['passbookimg']
        registerno = request.POST['registerno']
        

        newclub = CustomerCare(user_id=user,
                             IFSCcode=IFSCcode,
                             accountname=accountname,
                             accountnumber=accountnumber,
                             passbookimg=passbookimg,
                             registerno=registerno
                            )
        newclub.save()
    
        messages.success(request, "Bank Detail Created")
        return redirect('/homepage/createbankdetail/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createcustomerservice.html", {'users': user})





def UpdateCustomerCare(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        registeruser = request.POST['registeruser']
        IFSCcode = request.POST['IFSCcode']
        accountname = request.POST['accountname']
        accountnumber = request.POST['accountnumber']
        # passbookimg = request.FILES['passbookimg']
        
        uplead = CustomerCare.objects.filter(id=id)
        
        uplead.update(registeruser_id=registeruser,
                             IFSCcode=IFSCcode,
                             accountname=accountname,
                             accountnumber=accountnumber,
                            #  passbookimg=passbookimg
                        )
        messages.success(request, f"{accountname}, Bank details updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = CustomerCare.objects.get(id=id)    
        user = user_registration.objects.all()
        return render(request, "editcustomerservice.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailCustomerCare(request, id):
       mywithdraw = CustomerCare.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteCustomerCare(request, id):
    data = CustomerCare.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getallcustomercare/')



 
 
def CreateGetClubByUserView(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        clubid = request.POST['clubid']
        

        newclub = GetClubByUser(userid_id=userid,
                             clubid_id=clubid
                            )
        newclub.save()
    
        messages.success(request, "Bank Detail Created")
        return redirect('/homepage/creategetclubbyuser/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "clubbyuser.html", {'users': user})



def UpdateGetClubByUser(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        userid = request.POST['userid']
        clubid = request.POST['clubid']
        
        uplead = GetClubByUser.objects.filter(id=id)
        
        uplead.update(userid_id=userid,
                             clubid_id=clubid
                        )
        messages.success(request, "updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = GetClubByUser.objects.get(id=id)    
        user = user_registration.objects.all()
        getclub = club.objects.all()
        return render(request, "editclubuser.html", {'mypay':mypay, 'users': user, 'getclub':getclub})
    # return render(request, "edituser.html")



def DetailGetClubByUser(request, id):
       mywithdraw = GetClubByUser.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteGetClubByUser(request, id):
    data = GetClubByUser.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getclubbyuser/')







def CreateGetClubCloseView(request):
    if request.method == 'POST':
        clubclose = request.POST['clubclose']
        commission = request.POST['commission']
        

        newclub = ClubClosedTime(clubclose=clubclose,
                             commission=commission
                            )
        newclub.save()
    
        messages.success(request, "Club Closed Detail Created")
        return redirect('/homepage/creategetclubclose/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createclubclose.html", {'users': user})



def UpdateGetClubClose(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        clubclose = request.POST['clubclose']
        commission = request.POST['commission']
        
        uplead = ClubClosedTime.objects.filter(id=id)
        
        uplead.update(clubclose=clubclose,
                             commission=commission
                        )
        messages.success(request, "updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = ClubClosedTime.objects.get(id=id)    
        user = user_registration.objects.all()
        # getclub = club.objects.all()
        return render(request, "editclubclose.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailClubCloseTime(request, id):
       mywithdraw = ClubClosedTime.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteGetClubClose(request, id):
    data = ClubClosedTime.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getcloseclub/')



def CreateAvgTrasferTimeView(request):
    if request.method == 'POST':
        trasfertime = request.POST['trasfertime']
        commission = request.POST['commission']
        

        newclub = AvgTrasferTime(trasfertime=trasfertime,
                             commission=commission
                            )
        newclub.save()
    
        messages.success(request, "Average Transfer Detail Created")
        return redirect('/homepage/creategettransfer/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createavgtransfertime.html", {'users': user})



def UpdateAvgTrasferTime(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        trasfertime = request.POST['trasfertime']
        commission = request.POST['commission']
        
        uplead = AvgTrasferTime.objects.filter(id=id)
        
        uplead.update(trasfertime=trasfertime,
                             commission=commission
                        )
        messages.success(request, "updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = AvgTrasferTime.objects.get(id=id)    
        user = user_registration.objects.all()
        # getclub = club.objects.all()
        return render(request, "editavgtransfer.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailAvgTrasferTime(request, id):
       mywithdraw = AvgTrasferTime.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteAvgTrasferTime(request, id):
    data = AvgTrasferTime.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getavgtransfer/')




def CreateAmountTrasferTimeView(request):
    if request.method == 'POST':
        account_tran = request.POST['account_tran']
        commission = request.POST['commission']
        

        newclub = AmountTrasferTime(account_tran=account_tran,
                             commission=commission
                            )
        newclub.save()
    
        messages.success(request, "Average Transfer Detail Created")
        return redirect('/homepage/createamttransfer/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "createamounttransfer.html", {'users': user})



def UpdateAmountTrasferTime(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        account_tran = request.POST['account_tran']
        commission = request.POST['commission']
        
        uplead = AmountTrasferTime.objects.filter(id=id)
        
        uplead.update(account_tran=account_tran,
                             commission=commission
                        )
        messages.success(request, "updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = AmountTrasferTime.objects.get(id=id)    
        user = user_registration.objects.all()
        # getclub = club.objects.all()
        return render(request, "editamounttransfer.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailAmountTrasferTime(request, id):
       mywithdraw = AmountTrasferTime.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteAmountTrasferTime(request, id):
    data = AmountTrasferTime.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getamttransfer/')



def CreateAppNotificationView(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        clubid = request.POST['clubid']
        

        newclub = AppNotification(userid_id=userid,
                             clubid_id=clubid
                            )
        newclub.save()
    
        messages.success(request, "Bank Detail Created")
        return redirect('/homepage/creategetclubbyuser/')
    
    else:
        user = user_registration.objects.all()
        return render(request, "clubbyuser.html", {'users': user})



def UpdateAppNotification(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        userid = request.POST['userid']
        clubid = request.POST['clubid']
        
        uplead = AppNotification.objects.filter(id=id)
        
        uplead.update(userid_id=userid,
                             clubid_id=clubid
                        )
        messages.success(request, "updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = AppNotification.objects.get(id=id)    
        user = user_registration.objects.all()
        # getclub = club.objects.all()
        return render(request, "editclubuser.html", {'mypay':mypay, 'users': user})
    # return render(request, "edituser.html")



def DetailAppNotification(request, id):
       mywithdraw = AppNotification.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeleteAppNotification(request, id):
    data = AppNotification.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getclubbyuser/')



# def CreatePaymentrecordView(request):
#     if request.method == 'POST':
#         userid = request.POST['userid']
#         clubid = request.POST['clubid']
        

#         newclub = paymentrecord(userid_id=userid,
#                              clubid_id=clubid
#                             )
#         newclub.save()
    
#         messages.success(request, "Bank Detail Created")
#         return redirect('/homepage/creategetclubbyuser/')
    
#     else:
#         user = user_registration.objects.all()
#         return render(request, "clubbyuser.html", {'users': user})



def UpdatePaymentrecord(request, id):
    # my_users = User.objects.all()
    # print(my_users)
    if request.method == 'POST':
        roundpayment = request.POST['roundpayment']
        winner = request.POST['winner']
        looser = request.POST['looser']
        payamount = request.POST['payamount']
        payment_time = request.POST['payment_time']
        is_paid = request.POST['is_paid']
        
        uplead = paymentrecord.objects.filter(id=id)
        
        uplead.update(roundpayment_id=roundpayment,
                             winner_id=winner,
                             looser_id=looser,
                             payamount=payamount,
                             payment_time=payment_time,
                             is_paid=is_paid
                        )
        messages.success(request, "updated successfully")
        # return redirect('/homepage/getcashwallet/')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))    #redirect same  page
    else:
        mypay = paymentrecord.objects.get(id=id)    
        user = user_registration.objects.all()
        myround = rounds.objects.all()
        # getclub = club.objects.all()
        return render(request, "editpayment.html", {'mypay':mypay, 'users': user, 'rounds':myround})
    # return render(request, "edituser.html")



def DetailPaymentrecord(request, id):
       mywithdraw = paymentrecord.objects.get(id=id)
       getUser = user_registration.objects.all()
       for i in getUser:
           print(i.id)
    #    user = user_registration.objects.get(id=id)
    #    print(user)
    #    push_notify()
       return render(request, "viewdetail.html", {'mywithdraw':mywithdraw, 'adduser':getUser})
   
   
   
def DeletePaymentrecord(request, id):
    data = paymentrecord.objects.get(id=id)
    data.delete()
    # messages.success(request, f"{data.remarks}, Lead Deleted Succsessfull")
    return redirect('/homepage/getpaymentlist/')