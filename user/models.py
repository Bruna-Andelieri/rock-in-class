from django.db import models

# Create your models here.
class User(models.Model):
    name =  models.CharField(max_length=200, unique=True)
    email =  models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    