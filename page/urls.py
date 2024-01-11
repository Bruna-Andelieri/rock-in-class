
from django.urls import path
from .views import (
    page_index, 
    page_tutor,
    page_lesson, 
    page_register, 
    page_auth, 
    page_contact, 
    page_about, 
)

urlpatterns = [
    path("", page_index, name="index"),
    path("tutor/", page_tutor, name="tutor"),
    path("lesson/", page_lesson, name="lesson"),
    path("register/", page_register, name="register"),
    path("auth/", page_auth, name="auth"),
    path("contact/", page_contact, name="contact"),
    path("about/", page_about, name="about"),
]
