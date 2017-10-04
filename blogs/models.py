from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blogs(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Email = models.CharField(max_length=100, null=True, blank=True)

class UserProfile(models.Model):
    UserName =  models.ForeignKey(User)
    PhoneNumber = models.integer(max_length=100)
    Address = models.CharField(max_length=200)
