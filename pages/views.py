from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from booking.models import Booking
from booking.forms import UserForm
from tutor.models import Tutor

# Create your views here.
def page_index(request):
    tutors = Tutor.objects.all().order_by('-id')[:3]
    return render(request, "pages/index.html", {"tutors": tutors})


def page_about(request):
    return render(request, "pages/about.html")


@login_required
def page_profile(request):
    """
    renders profile page and requests all bookings
    """
    if request.method == 'POST':
        formulario = UserForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Porfile update successfuly')
            return redirect('profile')
        else: 
            messages.error(request, 'Failed to update data user.')
    else:

        form = UserForm(instance=request.user)

    student = request.user.id
    bookings = Booking.objects.filter(student=student).all()
    return render(request, "pages/profile.html",
                    {"form": form, 'bookings': bookings})


def error_404(request, exception):
    return render(request, 'pages/404.html')