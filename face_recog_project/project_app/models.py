
from distutils.command.upload import upload
from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Person(models.Model):
    Photo = models.ImageField(upload_to = "Personal_tof", default='Personal_tof' )
    Name = models.CharField(max_length= 200, default="Some String")
    School = models.CharField(max_length= 200, default="Some String")
    Department = models.CharField(max_length= 200, default="Some String")
    Email = models.CharField(max_length= 200, default="Some String")
    Address = models.CharField(max_length= 200, default="Some String")
    Contact = models.CharField(max_length= 200, default="Some String")

class UploadImage(models.Model):  
    image = models.ImageField(upload_to='images')  
  
    
class MultipleImage(models.Model):
    images = models.FileField(upload_to = 'folder')
    
class WebImage(models.Model):  
    images = models.ImageField(upload_to = 'webPics') 


class GetUrl(models.Model):
    Url = models.CharField(max_length= 1000000)

class Download(models.Model):
    file = models.FileField(upload_to = 'download')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()