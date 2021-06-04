from django.contrib import admin
from django.contrib.admin import options
from django.contrib.admin.filters import ListFilter
from django.db.models.query_utils import FilteredRelation
from django.utils.html import format_html

admin.site.site_header = "Tripple M group - Easy Apply"
# Register your models here.
from . import models
from .models import User, Job,CV,Education,Skill,Experience


class JobAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'specialist', 'deadline_date','users',)
    list_display = ('title', 'description', 'specialist', 'deadline_date' ,'click_me')
    list_filter = ('specialist', 'deadline_date')

    def click_me(self , obj):
        return format_html('<a> View </a>')
        
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name' , 'email' , 'phone'  , 'married' , 'gender' , 'jobs' , 'cv')
    fields = ['first_name', 'last_name' , 'email' , 'phone'  , 'married' , 'gender' ]    


class CV_Admin(admin.ModelAdmin):
    list_display = ('user', 'specialist' , 'nationality' , 'driving' ,)
    list_filter = ('specialist',)

class EduAdmin(admin.ModelAdmin):
    list_display = ('title' , 'description' , 'date' , 'cv')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill' ,'cv')
    list_filter = ('cv',)

class ExpAdmin(admin.ModelAdmin):
    list_display = ('title' , 'description' , 'cv')


admin.site.register(User , UserAdmin)
admin.site.register(Job , JobAdmin)
admin.site.register(CV , CV_Admin)
admin.site.register(Education , EduAdmin)
admin.site.register(Skill , SkillAdmin)
admin.site.register(Experience , ExpAdmin)