from django.db import models
from cloudinary.models import CloudinaryField


class Instrument(models.Model):
    name =  models.CharField(max_length=50, unique=True)


class MusicStyle(models.Model):
    name =  models.CharField(max_length=50, unique=True)


# Create your models here.
class Tutor(models.Model):
    name =  models.CharField(max_length=200, unique=True)
    email =  models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=50)
    avatar_image = CloudinaryField('image', default='placeholder')
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    music_styles = models.ForeignKey(MusicStyle, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
