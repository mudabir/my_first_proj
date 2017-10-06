from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user =  models.ForeignKey(User)
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=200)

class ProductPurchase(models.Model):
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    title =  models.CharField(max_length=200)
    price = models.IntegerField(default=0)

class ExampleModel(models.Model):
    model_pic = models.ImageField()

