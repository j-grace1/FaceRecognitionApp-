from django.urls import path
from . import views
from .views import Info_page, image_request 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('image_request', views.image_request, name = "image-request"),
    path('image_web/', views.image_web, name = "image_web"),
    path('test', views.test, name = "test"), 
    path('delete_book', views.delete_book, name = "delete_book"), 
    path('Info_page', views.Info_page, name = "Info_page"), 
     path('upload/', views.upload, name="upload")
]