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

def get_all_users():
    all_users = User.objects.all
    return all_users

def git_this_user_by_id(user_id):
    this_user = User.objects.get(id = user_id)
    return this_user

def git_this_user_by_email(email):
    this_user = User.objects.get(email = email)
    return this_user

def get_all_jobs():
    all_jobs = Job.objects.all
    return all_jobs

def get_this_job_by_id(job_id):
    this_job = Job.objects.get(id = job_id)
    return this_job

def get_this_job_by_specialist(specialist):
    this_job = Job.objects.filter(specialist = specialist)
    return this_job


def get_all_cvs():
    all_cvs = CV.objects.all
    return all_cvs

def get_user_cv(user_id):
    this_user = git_this_user_by_id(user_id)
    cv = this_user.cv
    return cv

def get_all_skills():
    all_skills = Skill.objects.all
    return all_skills

def get_all_experiences():
    all_experiences = Experience.objects.all
    return all_experiences

def apply_to_job(user_id, job_id):
    this_user = git_this_user_by_id(user_id)
    this_job = get_this_job_by_id(job_id)
    apply = this_job.users.add(this_user)

