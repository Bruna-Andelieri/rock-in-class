from django.contrib import admin
from django.urls import path, include
from .views import booking_form, booking_list

urlpatterns = [
    path("", booking_form),
    path("list/", booking_list),
]
