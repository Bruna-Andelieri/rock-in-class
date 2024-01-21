from datetime import datetime

from django.shortcuts import redirect, render
from django.contrib import messages

from tutor.models import Tutor
from booking.models import Booking
from booking.forms import BookingForm

# Create your views here.
def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, "tutor/tutor_list.html", {"tutors": tutors})


def tutor_detail(request, tutor_id):
 
    form = BookingForm()
    tutor = Tutor.objects.filter(id=tutor_id).first()  

    # format date to datepicker
    current_date = datetime.now().strftime('%Y-%m-%d')

    return render(request, "tutor/tutor_detail.html", {
        "form": form,
        "tutor": tutor, 
        "tutor_id": tutor_id, 
        "current_date": current_date 
    })
