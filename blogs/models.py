from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user =  models.ForeignKey(User)
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=200)



