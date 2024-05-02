from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager



class Donor(models.Model):
    blood_types = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    name = models.CharField(max_length=100)   
    email = models.EmailField(unique=True)
    blood_type = models.CharField(max_length=3, choices=blood_types)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    



class Event(models.Model):
    STATUS_CHOICES = (
        ('ongoing', 'On Going'),
        ('upcoming', 'Upcoming'),
        ('ended', 'Ended'),
    )

    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    

# class BloodRequest(models.Model):
#     BLOOD_TYPE_CHOICES = [
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#     ]

#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
#     age = models.PositiveIntegerField()
#     disease = models.CharField(max_length=200, blank=True)
#     need_within_date = models.DateField()
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name


# from django.db import models

class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Given', 'Given'),
        ('Not Available', 'Not Available'),
    ]

    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=100 , blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES,blank=True, null=True)
    age = models.PositiveIntegerField()
    disease = models.CharField(max_length=200, blank=True,null=True)
    need_within_date = models.DateField()
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='Processing')

    def __str__(self):
        return self.name

