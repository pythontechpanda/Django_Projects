from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    address = models.TextField(max_length=500)
    qualification = models.CharField(max_length=100)
    looking_for = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    display_picture = models.ImageField(upload_to='dp', blank=True, null=True)
    bg_picture = models.ImageField(upload_to='background', blank=True, null=True)
    contact_no = models.CharField(max_length=12)
    company_name = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    office_email = models.CharField(max_length=200)
    off_phone_no = models.CharField(max_length=12)
    upload_resume = models.FileField(upload_to='documents', blank=True, null=True)
    follower = models.ManyToManyField("Follow")
    
    

class Follow(models.Model):
    followed = models.ForeignKey(User, related_name='user_followers', on_delete=models.CASCADE)
    followed_by = models.ForeignKey(User, related_name='user_follows', on_delete=models.CASCADE)
    muted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.followed_by.username} started following {self.followed.username}"