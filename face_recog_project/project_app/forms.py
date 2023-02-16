from django.db import models  
from django.forms import fields  
from .models import UploadImage, GetUrl, MultipleImage  
from django import forms  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
  
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


class UserRegistrationForm(UserCreationForm):


    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )