from django.contrib import admin
from django.urls import path, include
from .views import delete_booking, edit_booking 


urlpatterns = [
     path('edit/<int:booking_id>', edit_booking, name='edit_booking'),
     path('delete/<int:booking_id>', delete_booking, name='delete_booking'),
]
