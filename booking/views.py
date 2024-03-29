from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import BookingEditForm, BookingForm, DeleteBookingForm
from .models import Booking
from tutor.models import Tutor


# Create your views here.
@login_required
def delete_booking(request, booking_id):
    """
    For deleting booking
    """
    # get booking object
    booking = get_object_or_404(Booking, pk=booking_id, student=request.user)

    if request.method == "POST":
        form = DeleteBookingForm(request.POST)
        if form.is_valid() and form.cleaned_data["delete"]:
            booking.delete()
            messages.success(request, "Booking deleted successful")
            return redirect("profile")
    else:
        form = DeleteBookingForm()

    return render(
        request,
        "booking/delete_booking.html",
        {"form": form, "booking_id": booking_id},
    )


@login_required
def edit_booking(request, booking_id):
    """
    For edit booking
    """
    # get booking object
    booking = get_object_or_404(Booking, pk=booking_id, student=request.user)

    if request.method == "POST":
        # create booking form
        form = BookingEditForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successful")
            return redirect("profile")

        else:
            messages.error(request, "Ops... Something goes wrong")
    else:
        # create a booking instance
        form = BookingEditForm(instance=booking)

    return render(
        request,
        "booking/edit_booking.html",
        {"form": form, "booking_id": booking_id},
    )


@login_required
def save_booking(request, tutor_id):
    """
    For save the booking
    """
    tutor = get_object_or_404(Tutor, id=tutor_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.student = request.user
            form.instance.tutor = Tutor.objects.get(pk=tutor_id)

            form.save()
            messages.success(request, "Booking updated successful")
            return redirect("index")

    else:
        form = BookingForm()

    return render(
        request,
        "tutor/tutor_detail.html",
        {"tutor": tutor, "tutor_id": tutor_id, "form": form},
    )
