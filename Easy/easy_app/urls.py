from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login' , views.login),
    path('registration',views.registration),
    path('reg',views.reg),
    path('log',views.log),
    path('user',views.user),
    path('to_be_created/<int:id>',views.create_request),
    path('create_cv',views.create_cv),
    path('view' ,views.cv_view),
    path('showjob',views.showjob),
    path('logout/',views.logout),
    path('add_edu', views.add_edu),
    path('create_cv/driving' , views.driving),
    path('create_cv/married' , views.married),
    path('create_cv/gender' , views.gender),
]