from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
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
    name=models.CharField(max_length=100,blank=True)
    qualification=models.CharField(max_length=100,blank=True)
    experience=models.CharField(max_length=200,blank=True)
    GENDER_CHOICES=[
            ("male","male"),
            ("female","female")
        ]
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default="male")
    bio=models.TextField(null=True)

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_profile")
    name=models.CharField(max_length=100,blank=True)
    qualification=models.CharField(max_length=200,blank=True)
    GENDER_CHOICES=[
        ("male","male"),
        ("female","female")
    ]
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default="male")
    date_of_birth=models.DateField(null=True)
    address=models.TextField(null=True)
    skills=models.TextField(null=True)
    college_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender,instance,created,**kwargs):
    if created:
        if instance.role=="student":
            StudentProfile.objects.create(user=instance)
        elif instance.role=="trainer":
            TrainerProfile.objects.create(User=instance)
post_save.connect(create_profile,sender=User)



