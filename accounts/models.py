from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=15)
    ROLE_CHOICES=[
        ("trainer","trainer"),
        ("student","student")
    ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

class TrainerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="trainer_profile")
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=200)
    bio=models.TextField(null=True)

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_profile")
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    date_of_birth=models.DateField(null=True)
    address=models.TextField(null=True)
    skills=models.TextField(null=True)
    college_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username
    
       
