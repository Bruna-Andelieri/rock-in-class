
from django.urls import path
from .views import (
    tutor,
    tutor_detail
)

urlpatterns = [
    path("", tutor, name="tutor"),
    path("detail", tutor_detail, name="tutor_detail"),
   
]
