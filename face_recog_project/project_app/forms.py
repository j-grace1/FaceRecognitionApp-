from django.db import models  
from django.forms import fields  
from .models import UploadImage, GetUrl, MultipleImage  
from django import forms  

  
  
class UserImageForm(forms.ModelForm):  

    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage
        # It includes all the fields of model  
        fields = '__all__'  
class web_photo(forms.ModelForm):  

    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage
        # It includes all the fields of model  
        fields = '__all__'  
class MultipleImage(forms.ModelForm):  

    class Meta:  
        # To specify the model to be used to create form  
        model = MultipleImage
        # It includes all the fields of model  
        fields = '__all__'  
        
class UrlForm(forms.ModelForm):  

    class Meta:  
        # To specify the model to be used to create form  
        model = GetUrl
        # It includes all the fields of model  
        fields = '__all__'  
        