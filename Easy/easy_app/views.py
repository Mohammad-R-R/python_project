from django.http import request
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
from time import strftime


# Create your views here.
def home(request):
    if 'id' in request.session:
        return redirect(f'/user/{request.session["id"]}')
    else:
        return render(request, "home.html")


def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')
    
def reg(request):
    errors = models.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        birthday=request.POST['birthday']
        email=request.POST['email']
        phone = request.POST['phone']
        password=pw_hash
        models.create_user(first_name,last_name,birthday,email,password,phone)
        this_user = models.get_this_user_by_email(email)
        request.session['id']=this_user[0].id
        request.session['f_name']=this_user[0].first_name
        request.session['l_name']=this_user[0].last_name
        date = this_user[0].birthday
        request.session['birthday']= date.strftime('%Y-%m-%d')
        request.session['email']=this_user[0].email                        
        return redirect(f'/user/{request.session["id"]}')

def log(request):
    email = request.POST['email']
    password = request.POST['password']
    errors = models.login_user(email , password)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/login')

    user = models.get_this_user_by_email(request.POST['email'])
    if 'login' not in request.session: #if user already logged in before
        request.session['f_name'] = user[0].first_name
        request.session['l_name'] = user[0].last_name
        request.session['email'] = user[0].email
        request.session['phone']=user[0].phone
        request.session['id'] = user[0].id
        print(request.session['f_name'])
        return redirect('/test2')
    else:
        return redirect('/login')

def user(request, id):
    if 'id' in request.session:
        return render(request, 'user.html')
    else:
        return redirect("/")

def cv_test(request):
    return render(request,'cv_builder.html')

def CV_test(request):
    return render(request,'create_CV.html')

    
def create_request(request,id):
    print("###########################################################################################################")
    nationality = request.POST['nationality']
    specialist = request.POST['specialist']
    driving=request.POST['driving']
    print("1111111111111111111111111111111111111111111111")
    id = request.session['id']
    print(id)
    print("2222222222222222222222222222222222222222222222222")
    models.add_to_builder(id,nationality,specialist,driving)
    return redirect(f"/view/{request.session['id']}")

def showjob(request):
    return render(request,'showjob.html')

def logout(request):
    request.session.clear()
    return redirect('/')
