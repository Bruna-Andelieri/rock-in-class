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
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            # Acesse um campo específico usando cleaned_data
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']
            form.instance.student = request.user
            tutor = Tutor.objects.get(pk=tutor_id)
            form.instance.tutor = tutor

            current_date = datetime.now().date()
            current_time = datetime.now().time()
  
            if booking_date <= current_date and booking_time <= current_time:
                messages.error(request, 'Booking should be greather than today')
        
            # check if tutor has booking
            booking = Booking.objects.filter(tutor_id=tutor_id, booking_date=booking_date, booking_time=booking_time).first()
            if booking:
                messages.error(request, 'This tutor already have schendule on this date/time')

            else:
                form.save()
                messages.success(request, 'Booking scheduled successfuly')
                return redirect('index')
            
    else:
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
