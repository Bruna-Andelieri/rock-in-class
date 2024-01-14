from django.shortcuts import render
from tutor.models import Tutor

# Create your views here.
def tutor(request):
    tutors = Tutor.objects.all()
    return render(request, "tutor.html", {"tutors": tutors})


def tutor_detail(request):
    return render(request, "tutor_detail.html")
