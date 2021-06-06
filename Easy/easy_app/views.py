from django.http import request
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
import bcrypt
from time import strftime


# Create your views here.
def home(request):
    if 'id' in request.session:
        return redirect('/user')
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
        return redirect('/user')

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
        return redirect('/user')
    else:
        return redirect('/login')

def user(request):
    if 'id' in request.session:
        context = {
        'user_cv': models.get_user_cv(request.session['id']),
        'this_user': models.get_this_user_by_id(request.session['id']),
        'all_jobs': models.get_all_jobs()
        }
        print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        for job in context['all_jobs']:
            print(job.users)
        print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
        return render(request, 'user.html' , context)
    else:
        return redirect("/")

def cv_view(request):
    context = {
        'user' : models.get_this_user_by_id(request.session['id']),
        'cv': models.get_user_cv(request.session['id']),
    }
    return render(request,'cv_view.html',context)

def create_cv(request):
    context = {
        'user_cv': models.get_user_cv(request.session['id']),
        'this_user': models.get_this_user_by_id(request.session['id'])
    }
    
    return render(request,'create_CV.html',context)
    
def create_request(request,id):
    nationality = request.POST['nationality']
    specialist = request.POST['specialist']
    # driving=request.POST['driving']
    id = request.session['id']
    models.add_to_builder(id,nationality,specialist,driving)
    return redirect("/create_cv")

def showjob(request):
    return render(request,'showjob.html')

def add_edu(request):
    edu = request.POST
    print("*"*50)
    print(edu)
    print("*"*50)
    return redirect('/create_cv')

def driving(request):
    user = models.get_this_user_by_id(request.session['id'])
    user.cv.driving = request.POST['driving']
    user.cv.save()
    return redirect('/create_cv')

def married(request):
    user = models.get_this_user_by_id(request.session['id'])
    user.married = request.POST['married']
    user.save()
    return redirect('/create_cv')

def gender(request):
    user = models.get_this_user_by_id(request.session['id'])
    user.gender = request.POST['gender']
    user.save()
    return redirect('/create_cv')

def logout(request):
    request.session.clear()
    return redirect('/')


