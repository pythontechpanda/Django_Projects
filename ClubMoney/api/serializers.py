from rest_framework import serializers
from .models import *



class user_serializer(serializers.ModelSerializer):
    profileimg=serializers.ImageField(max_length=None,allow_empty_file=True, required=False, use_url=True)
    class Meta:
        model = user_registration
        # fields = ['id', 'full_name', 'mobileno', 'city', 'password','gender','occupation','organisation','motive','income', 'monthlycontribution','profileimg']
        fields = ['id', 'full_name', 'mobileno', 'city', 'password','gender','occupation','motive','income', 'wallet_amount', 'monthlycontribution','profileimg','email','alternateno', 'token','create_at']
        
        
        
class userkyc_serializer(serializers.ModelSerializer):
        aadharfrontimg=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
        aadharbackimg=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
        panimg=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)

        class Meta:
            model = userkyc
            fields = ['id', 'registeruser', 'fullname', 'email','address','mobile', 'aadharno', 'aadharfrontimg','aadharbackimg', 'panno','panimg','is_verified']
            # fields = '__all__' 
            # depth = 1
# qs = userkyc.objects.all()
# print(userkyc_serializer(qs, many=True).data)

class bank_serializer(serializers.ModelSerializer):
        # registeruser = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='profile')
        passbookimg=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)

        class Meta:
            model = bankdetail
            # fields = ['id', 'registeruser', 'registerno', 'IFSCcode','accountname', 'accountnumber','passbookimg']
            fields = '__all__'
            depth = 1


class club_serializer(serializers.ModelSerializer):
        clubimage=serializers.ImageField(max_length=None, use_url=True)
        # r= club_serializer(club, many = True, email= email)
        class Meta:
            model = club
            fields = ['id', 'clubname','clubimage','clubamount','clubmembers', 'clubcontribution','startdate', 'starttime','duration','is_completed']
            depth = 1

class LevelsField(serializers.Field):
    
    def to_representation(self, value):
        return [value.level]

    def to_internal_value(self, data):
        # here you need to implement your transform logic
        return ','.join(data)

class club_serializer1(serializers.ModelSerializer):
        # clubimage=serializers.ImageField(max_length=None, use_url=True)
        # r= serializers.ListField()
        class Meta:
            model = rounds
            fields = ['roundname']
            
class round_serializer(serializers.ModelSerializer):
        # items = serializers.RelatedField(many=True)items = serializers.RelatedField(many=True)
        # clubname = serializers.CharField(source='club.clubname')
        class Meta:
            model = rounds
            fields = ['id', 'clubname','roundno', 'roundname', 'minbid','maxbid', 'winner','roundamount','status','startdate', 'starttime','duration','Payment_status','is_completed']
            # fields = '__all__'
            depth = 1
            
class inviteuser_serializer(serializers.ModelSerializer):
        # clubname = club_serializer(many=True, read_only=True)
        # invitemembers = user_serializer(read_only=True)
        class Meta:
            model = invite_user
            # fields = ['id', 'clubname','inviteto', 'is_join']
            fields = '__all__'
            depth = 1
            
            
class Issue_messages_Serializer(serializers.ModelSerializer):
    
    class Meta:
            model = IssueMessages
            fields = ['id', 'issue']         
            
            
class CustomerCare_serializer(serializers.ModelSerializer):
    
    # user = user_serializer(many=True)
    # issue = Issue_messages_Serializer(many=True)
    class Meta:
            model = CustomerCare
            # fields = ['id', 'user','issue', 'discription']
            fields = '__all__'
            depth = 1


class AddMoneySerializer(serializers.ModelSerializer):
    walletimg=serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True,required=False)
    class Meta:
            model = AddMoney
            # fields = '__all__'
            fields = ['id', 'userwallet', 'walletamount', 'walletimg', 'payment_status']
            # depth = 1
            
class WithdrawMoneySerializer(serializers.ModelSerializer):
    class Meta:
            model = WithdrawMoney
            # fields = '__all__'
            fields = ['id', 'userwallet', 'withdrawamount', 'payment_status']
            # depth = 1
        
class clubuserSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    club=serializers.CharField(max_length=200)
    clubname=serializers.CharField(max_length=200)
    clubimage=serializers.CharField(max_length=200)    
    clubamount=serializers.CharField(max_length=200)
    clubmembers=serializers.CharField(max_length=200)
    clubcontribution=serializers.CharField(max_length=200)
    startdate=serializers.CharField(max_length=200)
    starttime=serializers.CharField(max_length=200)
    duration=serializers.CharField(max_length=200)
    is_completed=serializers.CharField(max_length=200)
    clubuser=serializers.ListField(max_length=200)

class userclubSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    user=serializers.CharField(max_length=200)
    userclub=serializers.ListField(max_length=200)
    usermobileno=serializers.CharField(max_length=200)
    usercity=serializers.CharField(max_length=200)
    useroccupation=serializers.CharField(max_length=200)
    usermotive=serializers.CharField(max_length=200)
    userincome=serializers.CharField(max_length=200)
    userwallet_amount=serializers.CharField(max_length=200)
    usermonthlycontribution=serializers.CharField(max_length=200)
    userprofileimg=serializers.CharField(max_length=200)
    useremail=serializers.CharField(max_length=200)
    useralternateno=serializers.CharField(max_length=200)
    usercreate_at=serializers.CharField(max_length=200)
    total_subscription=serializers.CharField(max_length=200)
    


class AvgTrasferTimeSerializer(serializers.ModelSerializer):
    class Meta:
            model = AvgTrasferTime
            # fields = '__all__'
            fields = ['id', 'trasfertime', 'commission']
            
            
class AmountTrasferTimeSerializer(serializers.ModelSerializer):
    class Meta:
            model = AmountTrasferTime
            # fields = '__all__'
            fields = ['id', 'account_tran', 'commission']
            
            
            
class ClubClosedTimeSerializer(serializers.ModelSerializer):
    class Meta:
            model = ClubClosedTime
            # fields = '__all__'
            fields = ['id', 'clubclose', 'commission']
    
    
class GetClubByUserSerializer(serializers.ModelSerializer):
    class Meta:
            model = GetClubByUser
            # fields = '__all__'
            fields = ['id', 'clubuser', 'club']
            # depth = 1
            
            
class AppNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppNotification
        fields = ['id', 'usernotification', 'title', 'body', 'data', 'image', 'date']