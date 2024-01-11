from django.contrib import admin
from django.urls import path, include
from .views import user_form, user_list

urlpatterns = [
    path("", user_form),
    path("list/", user_list),
]
