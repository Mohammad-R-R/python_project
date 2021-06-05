from django.db import models
import re
import bcrypt


job_specialist = (("",""),('Engineering' , 'Engineering') , ('Doctor' , 'Doctor') , 
('Pharmacy' , 'Pharmacy') , ('IT' , 'IT') , ('Science' , 'Science') , 
('Math','Math') , ('Chemistry','Chemistry') , ('Biology','Biology'),
('Phisycs','Phisycs') , ('Sport','Sport') , ('Finance','Finance') , ('Managment','Managment'))


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["f_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["l_name"] = "last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"

        if postData["password"]!=postData['Confirm'] :
            errors['comfirm_pw']='the password does not match'
        if User.objects.filter(email=postData['email']):
            errors['Email']= 'This email is already used'

        return errors


sel_gender = (('Male','Male') , ('Female' , 'Female'))


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255 , unique=True)
    phone = models.IntegerField(unique=True)
    password=models.CharField(max_length=255)
    married = models.BooleanField(default=False)
    gender = models.CharField(choices= sel_gender, max_length=20,default="not specified")
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BlogManager()

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    specialist = models.CharField(choices= job_specialist ,max_length=255 ,default="" , blank=False)
    deadline_date = models.DateField()
    users = models.ManyToManyField(User , related_name="jobs" , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CV(models.Model):
    specialist = models.CharField(choices= job_specialist ,max_length=255 ,default="" , blank=False)
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

def validator(post_data):
    errors = User.objects.basic_validator(post_data)
    return errors


def create_user(first_name,last_name,birthday,email,password,phone):
    User.objects.create(first_name=first_name,last_name=last_name,birthday=birthday,email=email,password=password , phone=phone)

def get_all_users():
    all_users = User.objects.all
    return all_users

def get_this_user_by_id(user_id):
    this_user = User.objects.get(id = user_id)
    return this_user

def get_this_user_by_email(email):
    this_user = User.objects.filter(email = email)
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
    this_user = get_this_user_by_id(user_id)
    cv = this_user.cv
    return cv

def get_all_skills():
    all_skills = Skill.objects.all
    return all_skills

def get_all_experiences():
    all_experiences = Experience.objects.all
    return all_experiences

def apply_to_job(user_id, job_id):
    this_user = get_this_user_by_id(user_id)
    this_job = get_this_job_by_id(job_id)
    apply = this_job.users.add(this_user)



# -----------------------------------
def login_user(email , password):
    errors={}
    this_user = get_this_user_by_email(email)
    if len(this_user)>0:
        pw = this_user[0].password
        in_pw =  bcrypt.checkpw(password.encode(), pw.encode())
        if in_pw == True:
                return errors
    errors['login'] = "Username or password is incorrect"
    return errors

