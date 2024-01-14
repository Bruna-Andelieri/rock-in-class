
from django.urls import path
from .views import (
    page_booking,
    page_index, 
    page_tutor,
    page_lesson, 
    page_contact, 
    page_about, 
)

urlpatterns = [
    path("", page_index, name="index"),
    path("tutor/", page_tutor, name="tutor"),
    path("lesson/", page_lesson, name="lesson"),
    path("contact/", page_contact, name="contact"),
    path("about/", page_about, name="about"),
    path("booking/", page_booking, name="booking"),
]
