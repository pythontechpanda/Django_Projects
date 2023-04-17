from django.shortcuts import render,HttpResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# from django.views.decorators.csrf import csrf_exemptfrom
from accounts.models import CustomUser


class RegistrationView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = CustomUser.objects.all()
        serializer = CustomUserSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = CustomUser.objects.get(id=id)
            serializer = CustomUserSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = CustomUserSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = CustomUser.objects.get(pk=id)
        serializer = CustomUserSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = CustomUser.objects.get(pk=id)
        serializer = CustomUserSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = CustomUser.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})




class CreditCardView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = CreditCards.objects.all()
        serializer = CreditCardsSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = CreditCards.objects.get(id=id)
            serializer = CreditCardsSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = CreditCardsSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = CreditCards.objects.get(pk=id)
        serializer = CreditCardsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = CreditCards.objects.get(pk=id)
        serializer = CreditCardsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = CreditCards.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    


class DematAccountsView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = DematAccounts.objects.all()
        serializer = DematAccountsSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = DematAccounts.objects.get(id=id)
            serializer = DematAccountsSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = DematAccountsSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = DematAccounts.objects.get(pk=id)
        serializer = DematAccountsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = DematAccounts.objects.get(pk=id)
        serializer = DematAccountsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = DematAccounts.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
class InvestmentsView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = Investment.objects.all()
        serializer = InvestmentSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Investment.objects.get(id=id)
            serializer = InvestmentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = InvestmentSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = Investment.objects.get(pk=id)
        serializer = InvestmentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = Investment.objects.get(pk=id)
        serializer = InvestmentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = Investment.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    


    
    

class ITRandTAXView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = ITRandTAX.objects.all()
        serializer = ITRandTAXSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = ITRandTAX.objects.get(id=id)
            serializer = ITRandTAXSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = ITRandTAXSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = ITRandTAX.objects.get(pk=id)
        serializer = ITRandTAXSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = ITRandTAX.objects.get(pk=id)
        serializer = ITRandTAXSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = ITRandTAX.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    

class BankAccountsView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = BankAccounts.objects.all()
        serializer = BankAccountsSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = BankAccounts.objects.get(id=id)
            serializer = BankAccountsSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = BankAccountsSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = BankAccounts.objects.get(pk=id)
        serializer = BankAccountsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = BankAccounts.objects.get(pk=id)
        serializer = BankAccountsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = BankAccounts.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
class CreditLineView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = CreditLine.objects.all()
        serializer = CreditLineSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = CreditLine.objects.get(id=id)
            serializer = CreditLineSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = CreditLineSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = CreditLine.objects.get(pk=id)
        serializer = CreditLineSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = CreditLine.objects.get(pk=id)
        serializer = CreditLineSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = CreditLine.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
class PersonalLoanView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = PersonalLoan.objects.all()
        serializer = PersonalLoanSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = PersonalLoan.objects.get(id=id)
            serializer = PersonalLoanSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = PersonalLoanSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = PersonalLoan.objects.get(pk=id)
        serializer = PersonalLoanSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = PersonalLoan.objects.get(pk=id)
        serializer = PersonalLoanSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = PersonalLoan.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
    
class PersonalDetailsView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = PersonalDetails.objects.all()
        serializer = PersonalDetailsSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = PersonalDetails.objects.get(id=id)
            serializer = PersonalDetailsSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = PersonalDetailsSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = PersonalDetails.objects.get(pk=id)
        serializer = PersonalDetailsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = PersonalDetails.objects.get(pk=id)
        serializer = PersonalDetailsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = PersonalDetails.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
class KYCDetailsView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = KYCDetails.objects.all()
        serializer = KYCDetailsSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = KYCDetails.objects.get(id=id)
            serializer = KYCDetailsSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = KYCDetailsSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = KYCDetails.objects.get(pk=id)
        serializer = KYCDetailsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = KYCDetails.objects.get(pk=id)
        serializer = KYCDetailsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = KYCDetails.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})
    
    
    
    
class LikeProductView(viewsets.ViewSet):
    def list(self, request):      # list - get all record
        stu = LikeProduct.objects.all()
        serializer = LikeProductSerializer(stu, many=True)    # many use for bulk data come 
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = LikeProduct.objects.get(id=id)
            serializer = LikeProductSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = LikeProductSerializer(data = request.data)  # form data conviert in json data
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        id = pk
        stu = LikeProduct.objects.get(pk=id)
        serializer = LikeProductSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Update'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        id = pk
        stu = LikeProduct.objects.get(pk=id)
        serializer = LikeProductSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Update'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = LikeProduct.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})