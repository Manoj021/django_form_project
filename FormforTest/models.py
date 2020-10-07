from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class from_details(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    degree = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
