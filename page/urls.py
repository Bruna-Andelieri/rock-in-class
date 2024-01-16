
from django.urls import path
from .views import (
    page_booking,
    page_index, 
    page_contact, 
    page_about, 
    page_profile,
)

urlpatterns = [
    path("", page_index, name="index"),
    path("contact/", page_contact, name="contact"),
    path("about/", page_about, name="about"),
    path("booking/", page_booking, name="booking"),
    path('profile/', page_profile, name='profile'),
]
