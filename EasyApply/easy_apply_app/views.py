from django.shortcuts import redirect, render,HttpResponse
from . import models
from easy_apply_app.models import *
from django.contrib import messages
# import bcrypt


# Create your views here.
def home(requset):
    return render(requset, "home.html")


def login(request):
    return render(request,'login.html')

def reeg(request):
    return render(request,'registration.html')
    
def reg(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        
        password = request.POST['password1']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)
        
        User.objects.create(first_name= request.POST['first_name'],last_name = request.POST['last_name'],birthday=request.POST['Birthday'],email=request.POST['email'],password=pw_hash)
        

        users=User.objects.filter(email=request.POST['email'])
        logged_user=users[0]
        request.session['user']={
            'id':logged_user.id,
            'firstname':logged_user.first_name,
            'birthday':logged_user.Birthday,
            'last_name':logged_user.last_name,
            'email':logged_user.email
                        }
        return redirect('/welcome')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)
        
        User.objects.create(first_name= request.POST['first_name'],last_name = request.POST['last_name'],email=request.POST['email'],password=pw_hash)
        
        Use
        users=User.objects.filter(email=request.POST['email'])
        logged_user=users[0]
        request.session['user']={
            'id':logged_user.id,
            'firstname':logged_user.first_name,
            'last_name':logged_user.last_name,
            'email':logged_user.email
                        }
        # return redirect('/welcome')
        return render(request,'registration.html')

def user(request, id):
    return render(request, 'user.html')

def cv_test(request):
    return render(request,'cv_builder.html')

def CV_test(request):
    return render(request,'create_CV.html')

def showjob(request):
    return render(request,'showjob.html')
