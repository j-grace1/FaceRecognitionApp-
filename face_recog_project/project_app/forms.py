from django.db import models  
from django.forms import fields  
from .models import UploadImage, GetUrl, MultipleImage  
from django import forms  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
  
  
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
        
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user