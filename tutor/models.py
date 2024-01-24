from django.db import models
from cloudinary.models import CloudinaryField


class Instrument(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=6)


class MusicStyle(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=6)


# Create your models here.
class Tutor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    avatar_image = CloudinaryField(
        "image",
        default="https://res.cloudinary.com/difmdvoze/image/upload/v1705534784/static/images/placeholder.webp",
    )
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    music_styles = models.ForeignKey(MusicStyle, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
