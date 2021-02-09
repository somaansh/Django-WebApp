from django.contrib import admin
from django.urls import path
from webApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("register/", views.register, name='register'),
    path("contact/", views.contact, name='contact'),
    path("services/", views.services, name='services'),
    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    #path("successlogin/", views.logoutUser, name='logout'),
]