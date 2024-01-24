from django.urls import path
from .views import tutor_list, tutor_detail

urlpatterns = [
    path("", tutor_list, name="tutor"),
    path("<int:tutor_id>/", tutor_detail, name="tutor_detail"),
]
