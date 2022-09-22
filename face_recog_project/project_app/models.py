from asyncio.windows_events import INFINITE, NULL
from distutils.command.upload import upload
from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.db import models

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
    Url = models.CharField(max_length= INFINITE)

class Download(models.Model):
    file = models.FileField(upload_to = 'download')