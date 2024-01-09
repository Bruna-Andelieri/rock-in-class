from django.db import models
from tutor.models import Tutor
from tutor.models import User

# Create your models here.
class Schedule(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE,
                             related_name="schedule")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="schedule")
    when = models.DateTimeField(null=True)
    message =  models.CharField(max_length=200, unique=True)