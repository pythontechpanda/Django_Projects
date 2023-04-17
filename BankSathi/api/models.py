from django.db import models
from accounts.models import CustomUser

# Create your models here.



class CreditCards(models.Model):
    
    cardname = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    joinfees=models.CharField(max_length=25)
    annualfees=models.CharField(max_length=25)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    offer1=models.CharField(max_length=200, null=True)
    offer2=models.CharField(max_length=200, null=True)
    offer3=models.CharField(max_length=200, null=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='creaditcard/')
    active_status =  models.BooleanField(default=False)
    
class DematAccounts(models.Model):
    
    dematname = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='demat/')
    active_status =  models.BooleanField(default=False)


class Investment(models.Model):
    
    invname = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='invest/')
    active_status =  models.BooleanField(default=False)
    

class ITRandTAX(models.Model):
    
    name = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='itrandtax/')
    active_status =  models.BooleanField(default=False)
    
    
class BankAccounts(models.Model):
    
    bankname = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='bank/')
    active_status =  models.BooleanField(default=False)
    
    
class CreditLine(models.Model):
    
    clname = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='creditline/')
    active_status =  models.BooleanField(default=False)
    
    
class PersonalLoan(models.Model):
    
    psname = models.CharField(max_length=300)
    discription = models.CharField(max_length=300)
    earnupto=models.CharField(max_length=25)
    total_earn=models.CharField(max_length=50, blank=True)
    total_lead=models.CharField(max_length=50, blank=True)
    toatl_sale=models.CharField(max_length=50, blank=True)
    details = models.JSONField(blank=True,null=True)
    training = models.JSONField(blank=True,null=True)
    marketing = models.JSONField(blank=True,null=True)
    banklogo =models.FileField(blank=True,upload_to='psloan/')
    active_status =  models.BooleanField(default=False)
    

class PersonalDetails(models.Model):
    fullname = models.CharField(max_length=200) 
    mobileno = models.CharField(max_length=12)
    email = models.EmailField(max_length=300)
    pincode = models.CharField(max_length=10)
    dob = models.CharField(max_length=50)
    
    
class ProfessionalDetails(models.Model):
    working_as = models.CharField(max_length=200) 
    source_income = models.CharField(max_length=200) 
    total_experience = models.CharField(max_length=200) 
    


class KYCDetails(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    address=models.CharField(max_length=100)
    aadharno=models.CharField(max_length=50,unique=True)
    panno=models.CharField(max_length=50,unique=True)
    is_verified=models.BooleanField(default=False)
    
    
class LikeProduct(models.Model):
    author = models.ForeignKey(CreditCards, on_delete=models.CASCADE)
    like =  models.ManyToManyField(CustomUser, related_name="bank", default=None, blank=True)
    
    
    def __str__(self):
        return self.author.first_name
    
    @property
    def num_likes(self):
        return self.like.all().count()
    
    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked += 1
        return total_liked

    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.like.all().count()
        return total_liked
    
    
    
class URLThumbnil(models.Model):
    url = models.CharField(max_length=350)
    date = models.DateField(auto_now_add=True)
    