from urllib import request
from django.db import models
from django.contrib.auth.models import User

from tutor.models import Tutor


# Create your models here.
class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_student")
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name="booking_tutor")
    booking_date = models.DateField(null=False, blank=False)
    booking_time = models.CharField(null=False, blank=False, max_length=5)
    message =  models.CharField(null=True, max_length=200)