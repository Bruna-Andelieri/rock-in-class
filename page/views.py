from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from booking.models import Booking
from booking.forms import UserForm

# Create your views here.
def page_index(request):
    return render(request, "index.html")


def page_contact(request):
    return render(request, "contact.html")

def page_about(request):
    return render(request, "about.html")

def page_booking(request):
    return render(request, "booking.html")



@login_required
def page_profile(request):
    """
    renders profile page and requests all bookings
    """

    student = request.user.id
    bookings = Booking.objects.filter(student=student).all()

    if request.method == 'POST':
        formulario = UserForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Dados atualizados com sucesso.')
            return redirect('profile')
        else: 
            messages.error(request, 'Erro ao atualizar os dados do usuario.')
    else:
        form = UserForm(instance=request.user)

    return render(request, "profile.html",
                    {"form": form, 'bookings': bookings})