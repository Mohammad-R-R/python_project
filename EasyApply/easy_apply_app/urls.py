from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login' , views.login),
    path('register',views.register),
    path('user/<int:id>',views.user),
    path('test',views.cv_test),
    path('test2',views.CV_test),

]