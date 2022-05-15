
from django.urls import path

from BloodBankApp import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('Registration/',views.Registration,name='Registration'),
    path('Login/',views.Login,name='Login'),
    path('Donation/',views.Donation,name='Donation'),
    path('Logout/',views.Logout,name='Logout'),


]