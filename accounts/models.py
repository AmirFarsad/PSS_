from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    Firstname = models.CharField(max_length=50, null=False, blank=False, default="")
    Lastname = models.CharField(max_length=50, null=False, blank=False, default="")
    Birth = models.CharField(max_length=256,null=True, blank=True)
    Info = models.CharField(max_length=255, null=False, blank=True, default="")
    Job = models.CharField(max_length=50, null=False, blank=True, default="")
    ProfilePicture = models.ImageField(max_length=255, default='static\profile\assets\img\default_original_profile_pic.png', upload_to='profile\assets\img')
    CoverPicture = models.ImageField(max_length=255,default='static\profile\assets\img\need_cover.jpg')
    
    def __str__(self):
        return self.username

