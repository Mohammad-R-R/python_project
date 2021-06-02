from django.contrib import admin

admin.site.site_header = "Tripple M group - Easy Apply"
# Register your models here.
from . import models
from .models import User, Job,CV,Education,Skill,Experience

class OrganizerAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'specialist', 'deadline_date')

admin.site.register(User)
admin.site.register(Job , OrganizerAdmin)
admin.site.register(CV)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)