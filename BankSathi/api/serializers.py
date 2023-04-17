from rest_framework import serializers
from .models import *
from accounts.models import CustomUser

class CreditCardsSerializer(serializers.ModelSerializer):
        banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
        

        class Meta:
            model = CreditCards
            fields = ['id', 'cardname', 'discription','earnupto','total_earn', 'total_lead','toatl_sale', 'offer1', 'offer2', 'offer3', 'details','training','marketing','banklogo','joinfees', 'annualfees', 'active_status']
            
class DematAccountsSerializer(serializers.ModelSerializer):
    banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = DematAccounts
            fields = ['id', 'dematname', 'discription', 'earnupto','total_earn', 'total_lead','toatl_sale', 'details','training','marketing', 'banklogo', 'active_status']
    
            

class InvestmentSerializer(serializers.ModelSerializer):
    banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = Investment
            fields = ['id', 'invname', 'discription', 'earnupto','total_earn', 'total_lead','toatl_sale', 'details','training','marketing', 'banklogo', 'active_status']
            
            
class ITRandTAXSerializer(serializers.ModelSerializer):
    banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = ITRandTAX
            fields = ['id', 'name', 'discription', 'earnupto','total_earn', 'total_lead','toatl_sale', 'details','training','marketing', 'banklogo', 'active_status']
            

class BankAccountsSerializer(serializers.ModelSerializer):
    banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = BankAccounts
            fields = ['id', 'bankname', 'discription', 'earnupto','total_earn', 'total_lead','toatl_sale', 'details','training','marketing', 'banklogo', 'active_status']
            
            
class CreditLineSerializer(serializers.ModelSerializer):
    banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = CreditLine
            fields = ['id', 'clname', 'discription', 'earnupto','total_earn', 'total_lead','toatl_sale', 'details','training','marketing', 'banklogo', 'active_status']
            
            
            
class PersonalLoanSerializer(serializers.ModelSerializer):
    banklogo=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = PersonalLoan
            fields = ['id', 'psname', 'discription', 'earnupto','total_earn', 'total_lead','toatl_sale', 'details','training','marketing', 'banklogo', 'active_status']
            

class PersonalDetailsSerializer(serializers.ModelSerializer):
   
    class Meta:
            model = PersonalDetails
            fields = ['id', 'fullname', 'mobileno', 'email', 'pincode', 'dob']
            
            

class CustomUserSerializer(serializers.ModelSerializer):
       
    class Meta:
            model = CustomUser
            fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined']
            
            
class KYCDetailsSerializer(serializers.ModelSerializer):
       
    class Meta:
            model = KYCDetails
            fields = ['id', 'user', 'address', 'aadharno', 'panno', 'is_verified']
            depth = 1
            
            
class LikeProductSerializer(serializers.ModelSerializer):
       
    class Meta:
            model = LikeProduct
            fields = ['id', 'author', 'like']   
            # fields = "__all__"
            # depth = 1