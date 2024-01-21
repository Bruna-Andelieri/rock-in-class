from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, DeleteBookingForm

from .models import Booking
from tutor.models import Tutor

# Create your views here.

@login_required
def delete_booking(request, booking_id):
    # get booking object
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        form = DeleteBookingForm(request.POST)
        if form.is_valid() and form.cleaned_data['delete']:
            booking.delete()
            return redirect('profile')  # Redirecione para onde desejar após a exclusão
    else:
        form = DeleteBookingForm()

    return render(request, 'booking/delete_booking.html', {'form': form, 'booking_id': booking_id})

    


@login_required
def edit_booking(request, booking_id):
    # get booking object
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        # create booking form
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successful")
            return redirect('profile')
        
        else:
            messages.error(request, "Ops... Something goes wrong")
    else:

        # create a booking instance
        form = BookingForm(instance=booking)

        # format data to datepicker
        formatted_date = booking.booking_date.strftime('%Y-%m-%d')
       

    return render(request, 'booking/edit_booking.html', {'form': form, "booking_id": booking_id, "formatted_date": formatted_date})



def save_booking(request, tutor_id):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            # Acesse um campo específico usando cleaned_data
            try:
                booking_date = form.cleaned_data['booking_date']
                booking_time = datetime.strptime(form.cleaned_data['booking_time'], '%H:%M').time()
            except RuntimeError as e:
                messages.error(request, 'Date / time format not valid.')
                return redirect('tutor_detail')
                print(e)


            form.instance.student = request.user
            tutor = Tutor.objects.get(pk=tutor_id)
            form.instance.tutor = tutor

            current_date = datetime.now().date()
            current_time = datetime.now().time()
  
            if booking_date <= current_date and booking_time <= current_time:
                messages.error(request, 'Booking should be greather than today')
                return redirect('tutor_detail')
        
            # check if tutor has booking
            booking = Booking.objects.filter(tutor_id=tutor_id, booking_date=booking_date, booking_time=booking_time).first()
            if booking:
                messages.error(request, 'This tutor already have schendule on this date/time')
                return redirect('tutor_detail')

            else:
                form.save()
                messages.success(request, 'Booking scheduled successfuly')
                return redirect('index')
            
        else:
            messages.error(request, 'Something goes wrong with booking. Please try it later')
        
        return redirect('index')
  