from django.urls import path,include
from . import views
from .views import Info_page, image_request,download_file, multiple_image_view, signup_view, activation_sent_view, activate, about_view
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from allauth.account.views import LoginView
from django.contrib.auth.views import PasswordResetForm, PasswordResetDoneView

from project_app import views as user_views





urlpatterns = [
    path('home/', views.index, name='index'),
    path('image_request', views.image_request, name = "image-request"),
    path('image_web/', views.image_web, name = "image_web"),
    path('test', views.test, name = "test"), 
    path('delete_book', views.delete_book, name = "delete_book"), 
    path('Info_page', views.Info_page, name = "Info_page"), 
     path('upload/', views.upload, name="upload"),
     path('download_file', views.download_file, name= "download_file"),
     path('multiple_image_view', views.multiple_image_view, name= "multiple_image_view"),
   path('register/', user_views.register, name='register'),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent_view"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
       path('accounts/', include('allauth.urls')),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('about/', views.about_view, name='about'),
     path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'),
        name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
]