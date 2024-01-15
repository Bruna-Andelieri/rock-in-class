
from django.urls import path
from .views import (
    tutor,
    tutor_detail
)

urlpatterns = [
    path("", tutor, name="tutor"),
    path("<int:tutor_id>/", tutor_detail, name="tutor_detail"),
]
