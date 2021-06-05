from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login' , views.login),
    path('registration',views.registration),
    path('reg',views.reg),
    path('log',views.log),
    path('user/<int:id>',views.user),
    path('test',views.cv_test),
    path('to_be_created/<int:id>/',views.create_request),
    path('test2',views.CV_test),
    path('showjob',views.showjob),
    path('logout/',views.logout)
]