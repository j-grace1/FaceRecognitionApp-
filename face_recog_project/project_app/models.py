from asyncio.windows_events import INFINITE, NULL
from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.

class Person(models.Model):
    title = models.CharField(max_length= 200)

class UploadImage(models.Model):  
    image = models.ImageField(upload_to='images')  
  
    
class MultipleImage(models.Model):
    images = models.FileField(upload_to = 'folder')
    
class WebImage(models.Model):  
    images = models.ImageField(upload_to = 'webPics') 


class GetUrl(models.Model):
    Url = models.CharField(max_length= INFINITE)