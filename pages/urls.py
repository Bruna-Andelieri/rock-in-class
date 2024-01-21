
from django.urls import path
from django.conf.urls import handler404

from .views import (
    page_index, 
    page_about, 
    page_profile
)

urlpatterns = [
    path("", page_index, name="index"),
    path("about/", page_about, name="about"),
    path('profile/', page_profile, name='profile'),
]


