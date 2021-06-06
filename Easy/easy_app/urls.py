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
    path('create_cv/delete/<int:edu_id>' ,views.delete_education),
    path('create_cv/delete_exp/<int:exp_id>' ,views.delete_experience),
    path('create_cv/delete_skill/<int:skill_id>' ,views.delete_skill),
    path('showjob',views.showjob),
    path('logout/',views.logout),
    path('add_edu', views.add_edu),
    path('add_exp', views.add_exp),
    path('add_skill', views.add_skill),
    path('create_cv/driving' , views.driving),
    path('create_cv/married' , views.married),
    path('create_cv/gender' , views.gender),
    path('showjob/<int:job_id>' , views.showjob),
    path('showjob/<int:job_id>/apply_job' , views.apply_job),
    path('showjob/<int:job_id>/withdraw' , views.withdraw),

]