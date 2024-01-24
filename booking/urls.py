from django.urls import path
from .views import delete_booking, edit_booking, save_booking


urlpatterns = [
    path("edit/<int:booking_id>", edit_booking, name="edit_booking"),
    path("delete/<int:booking_id>", delete_booking, name="delete_booking"),
    path("save/<int:tutor_id>", save_booking, name="save_booking"),
]
