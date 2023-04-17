from django.db import models
from itertools import islice
from rest_framework import serializers




class user_registration(models.Model):
    
    full_name=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50, unique=True)
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    # organisation=models.CharField(max_length=50)
    motive=models.CharField(max_length=100)
    income=models.CharField(max_length=50)
    wallet_amount= models.CharField(max_length=50,default='0')
    monthlycontribution=models.CharField(max_length=50)
    profileimg=models.ImageField(blank=True,null=True,upload_to='user/')
    email=models.CharField(max_length=50)
    alternateno=models.CharField(max_length=50,blank=True)
    token = models.CharField(max_length=300)
    create_at=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.full_name#, self.id

class userkyc(models.Model):
    registeruser=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=50)
    fullname = models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=250,null=True)
    aadharno=models.CharField(max_length=50,unique=True)
    aadharfrontimg=models.FileField(blank=True,upload_to='aadhar/',default='aadhar/none/no-img.jpg')
    aadharbackimg=models.FileField(blank=True,upload_to='aadhar/',default='aadhar/none/no-img.jpg')
    panno=models.CharField(max_length=50,unique=True)
    panimg=models.FileField(blank=True,upload_to='pan/',default='pan/none/no-img.jpg')
    is_verified=models.BooleanField(default=False)

class bankdetail(models.Model):
    registeruser=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    # mobileno=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    registerno=models.CharField(max_length=25,unique=True)
    IFSCcode=models.CharField(max_length=25)
    accountname=models.CharField(max_length=25)
    accountnumber=models.CharField(max_length=25,unique=True)
    passbookimg=models.FileField(blank=True,upload_to='passbook/',default='passbook/none/no-img.jpg')


class club(models.Model):
    # #user=models.ForeignKey(user_registration,on_delete=models.CASCADE, null=True, blank=True,related_name='clubCreater')
    clubname=models.CharField(max_length=50, unique=True)
    clubimage=models.FileField(upload_to='club/',default='club/none/no-img.jpg')
    clubamount=models.CharField(max_length=25)
    clubmembers=models.CharField(max_length=25)
    clubcontribution=models.CharField(max_length=20)
    startdate=models.DateField(null=True)
    starttime=models.TimeField(null=True)
    # duration=models.DurationField(null=True)
    duration=models.CharField(max_length=20,null=True)
    is_completed=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.clubname

class rounds(models.Model): 
    # user=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    clubname=models.CharField(max_length=50)
    roundno=models.CharField(max_length=20,null=True)
    roundname=models.CharField(max_length=20,null=True)
    minbid=models.CharField(max_length=20,null=True)
    maxbid=models.CharField(max_length=20,null=True)
    winner=models.CharField(max_length=20,null=True)
    roundamount=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    startdate=models.DateField(null=True)
    starttime=models.TimeField(null=True)
    duration=models.CharField(max_length=20,null=True)
    is_completed=models.BooleanField(null=True)
    Payment_status=models.BooleanField(default=False)

    def __str__(self):        
        return self.roundname #, self.id
    

class invite_user(models.Model):
    clubname=models.ForeignKey(club, on_delete=models.CASCADE, related_name='nameclub')
    inviteto=models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name='inviteuser')
    is_join=models.BooleanField(default=False)
    

class IssueMessages(models.Model):
    message = models.CharField(max_length=300,null=True)

    
class CustomerCare(models.Model):
    user = models.ForeignKey(user_registration,on_delete=models.CASCADE, related_name="sample")
    issue = models.ForeignKey(IssueMessages,on_delete=models.CASCADE, related_name="issue")
    #  = models.CharField(max_length=50,null=True)
    discription = models.CharField(max_length=500,null=True)
    status = models.BooleanField(default=False)
    

class bidding(models.Model):
    roundbid=models.ForeignKey(rounds, on_delete=models.CASCADE,null=True)
    biduser = models.ForeignKey(user_registration,on_delete=models.CASCADE)
    amount = models.CharField(max_length=30)

class cashwallet(models.Model):
    userwallet=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    walletamount=models.CharField(max_length=30,blank=True)
    walletimg=models.FileField(blank=True,upload_to='passbook/',default='passbook/none/no-img.jpg')
    casdate = models.DateField(auto_now=True)
    is_added=models.BooleanField(default=False)
    
    
class Withdrawcashwallet(models.Model):
    userwallet=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    walletamount=models.CharField(max_length=30,blank=True)
    # walletimg=models.FileField(blank=True,upload_to='passbook/',default='passbook/none/no-img.jpg')
    walletwithdraw=models.CharField(max_length=30,blank=True)
    date = models.DateField(auto_now=True)
    is_withdraw=models.BooleanField(default=False)
    
class AddMoney(models.Model):
    userwallet=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    walletamount=models.CharField(max_length=30)
    walletimg=models.FileField(blank=True,upload_to='passbook/',default='passbook/none/no-img.jpg')
    add_date = models.DateTimeField(auto_now=True)
    payment_status = models.BooleanField(default=False)
    
    
class WithdrawMoney(models.Model):
    userwallet=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    withdrawamount=models.CharField(max_length=30)
    withdraw_date = models.DateTimeField(auto_now=True)
    payment_status = models.BooleanField(default=False)

class GetClubByUser(models.Model):
    userid=models.ForeignKey(user_registration, on_delete=models.CASCADE)
    clubid=models.ForeignKey(club, on_delete=models.CASCADE)
    



class AvgTrasferTime(models.Model):
    trasfertime = models.CharField(max_length=200)
    commission = models.CharField(max_length=200)
    
    
class AmountTrasferTime(models.Model):
    account_tran = models.CharField(max_length=200)
    commission = models.CharField(max_length=200)
    
class ClubClosedTime(models.Model):
    clubclose = models.CharField(max_length=200)
    commission = models.CharField(max_length=200)



class AppNotification(models.Model):
    usernotification=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    title = models.CharField(max_length=300,null=True)
    body = models.CharField(max_length=300,null=True)
    data = models.CharField(max_length=500,null=True)
    image = models.FileField(blank=True,upload_to='notification/',default='notification/none/no-img.jpg',null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    


class paymentrecord(models.Model):
    roundpayment=models.ForeignKey(rounds,on_delete=models.CASCADE)
    winner=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='win')
    looser=models.ForeignKey(user_registration,on_delete=models.CASCADE,related_name='loose')
    payamount=models.CharField(max_length=20)
    is_paid=models.BooleanField(default=False)
    payment_time=models.CharField(max_length=50,null=True)