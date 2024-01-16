from django.contrib import admin
from django.urls import path, include
from .views import delete_booking, edit_booking 


urlpatterns = [
     path('edit/', edit_booking, name='edit_booking'),
     path('delete/', delete_booking, name='delete_booking'),
]
