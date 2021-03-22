from django.contrib import admin
from django.urls import path
from webApp import views

urlpatterns = [
    path("", views.index, name='home'),
    #path("register/", views.register, name='register'),
    path("contact/", views.contact, name='contact'),
    path("services/", views.services, name='services'),
    path("signup/", views.handleSignup, name='handleSignup'),
    path("login/", views.handleLogin, name='handleLogin'),
    path("logout/", views.handleLogout, name='handleLogout'),
    path("newlogin/", views.newLogin, name='newLogin')
]