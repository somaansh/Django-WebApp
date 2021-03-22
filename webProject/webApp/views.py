from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from webApp.models import Contact
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from webApp.models import Registration
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')
    

def handleSignup(request):
    if request.method == 'POST':
        #register = Registration()

        fullname = request.POST.get('fullname')
        photograph = request.POST.get('photograph')
        email_id = request.POST.get('email_id')
        phone_no = request.POST.get('phone_no')
        pswd = request.POST.get('pswd')
        Confirm_pswd = request.POST.get('Confirm_pswd')
        city_live = request.POST.get('city_live')
        state_live = request.POST.get('state_live')
        zip_code = request.POST.get('zip_code')
        id_card = request.POST.get('id_card')
         
        '''register.fullname = fullname
        register.photograph = photograph   
        register.email_id = email_id
        register.phone_no = phone_no
        register.email_id = email_id 
        register.pswd = pswd 
        register.Confirm_pswd = Confirm_pswd 
        register.city_live = city_live
        register.state_live = state_live 
        register.zip_code = zip_code 
        register.id_card = id_card'''

        if pswd !=  Confirm_pswd:
            messages.error(request, "Passwords do not match")
            return redirect('handleSignup')

        '''register.date = datetime.today() 
        register.save()
        messages.success(request, 'Registered Successfully! Please login now to continue.')'''

        user = User.objects.filter(email = email_id).first()

        if user:
            message = {'error' : 'user already exists'}
            context = message
            return render(request, 'register.html', context)
        #myuser = User.objects.create_user(fullname, email_id, pswd)
        myuser = User(first_name = fullname.split()[0], email = email_id, username = email_id )
        myuser.set_password(pswd)
        myuser.date = datetime.today()
        #myuser.fullname = fullname
        myuser.save()
        messages.success(request, 'Registered Successfully! Please login now to continue.')
        return redirect('home')

    else:
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

def handleLogin(request):
    if request.method == "POST":

        lgnemail = request.POST['loginemail']
        loginpassword = request.POST['loginpwsd']
        #checking authentication details....
        user = authenticate(username=lgnemail, password=loginpassword)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            #return render(request, 'quiz.html') 
            return redirect("/contact.html")
        else:
            # No backend authenticated the credentials 
            messages.error(request, 'Invalid Login. Please try again')
            return redirect('home') 

        
    return HttpResponse('404 - Not Found')


@login_required
def handleLogout(request):
    
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('home')


def newLogin(request):

    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('newlogin')
        else:
            print("2+2=4")
    else:
        return render(request, 'newlogin.html')

    
    
    