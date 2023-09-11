from django.urls import path
from . import views

urlpatterns = [
    path('salesforce_oauth/', views.salesforce_oauth, name='salesforce_oauth'),
    path('welcome/', views.welcome, name='welcome'),  
    path('callback/', views.callback, name='callback'),
     path('', views.home, name='home'),
  
   
   
]