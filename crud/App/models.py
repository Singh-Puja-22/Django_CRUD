from django.db import models

# Create your models here.

class Customer(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    number = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    pincode = models.IntegerField(null=True)
    image = models.ImageField(upload_to="static/images/", null = True)
