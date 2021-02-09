from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from webApp.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    return render(request, 'index.html')
    

def register(request):
    return render(request, 'register.html')
    

def contact(request):
    if request.method == "POST":
        contact = Contact()
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query') 
        #fname = request.POST.get('fname')
        #lname = request.POST.get('lname')
        #email = request.POST.get('email')
        #phone = request.POST.get('phone')
        #query = request.POST.get('query')
        #contact = Contact(fname=fname, lname=lname, email=email, phone=phone, query=query, date= datetime.today())
        contact.fname = fname 
        contact.lname = lname 
        contact.phone = phone 
        contact.email = email 
        contact.query = query 
        contact.date = datetime.today() 
        contact.save()
        messages.success(request, 'Your message has been recieved!. We will shortly contact you')
        return render(request, 'contact.html')
    return render(request, 'contact.html')
    

def services(request):
    return render(request, 'services.html')

#def register(request):
 #   form = UserCreationForm()
  #  context = {}
   # return render(request, 'register.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #checking authentication details....
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request, 'successlogin.html') 
        else:
            # No backend authenticated the credentials 
            return render(request, 'login.html') 

        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
    