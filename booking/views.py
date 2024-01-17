from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, DeleteBookingForm
from .models import Booking

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

        # Criar uma instância do formulário com a instância do objeto existente
        form = BookingForm(instance=booking)

    return render(request, 'booking/edit_booking.html', {'form': form, "booking_id": booking_id})
