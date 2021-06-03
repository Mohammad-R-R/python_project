from django.shortcuts import render

# Create your views here.
def home(requset):
    return render(requset, "home.html")

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'registration.html')

def user(request, id):
    return render(request, 'user.html')

def cv_test(request):
    return render(request,'cv_builder.html')

def CV_test(request):
    return render(request,'create_CV.html')

