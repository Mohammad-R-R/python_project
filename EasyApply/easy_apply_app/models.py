from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255 , unique=True)
    phone = models.IntegerField(unique=True)
    status = models.BooleanField()
    gender = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    specialist = models.CharField(max_length=255)
    deadline_date = models.DateField()
    users = models.ManyToManyField(User , related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CV(models.Model):
    specialist = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    driving = models.BooleanField()
    user = models.OneToOneField(User , related_name="cv" , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Education(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    date = models.DateField()
    cv = models.ForeignKey(CV, related_name="educations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    skill = models.TextField()
    cv = models.ForeignKey(CV, related_name="skills", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Experience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cv = models.ForeignKey(CV, related_name="experiences", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
