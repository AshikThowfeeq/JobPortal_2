from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import datetime



class User(AbstractUser):
      options = (
        ("candidate","candidate"),
        ("employer","employer") 
      )
      role = models.CharField(max_length=200,choices=options)
    
 
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="images",null=True)
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=200)
    resume = models.FileField(upload_to="resumes",null=True)
    location = models.CharField(max_length=200)
    ready_to_relocate = models.BooleanField(default=True)
    skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    logo = models.ImageField(upload_to="logos", null=True)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=200)
    adress =  models.CharField(max_length=300)
    company_name = models.CharField(max_length=200)
 
    def __str__ (self):
        return self.company_name
 
class Job(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    qualification=models.CharField(max_length=200)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    
 
    def __str__ (self):
        return self.title
 
class Application(models.Model):
    company = models.ForeignKey(CompanyProfile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    options = (
        ("pending","pending"),
		("accept","accept"),
		("reject","reject")
    )
    options = models.CharField(max_length=200,choices=options,default="pending")
    apply_date = models.DateField(auto_now_add=True)
 



