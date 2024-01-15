from django.shortcuts import redirect, render
from django.contrib import messages


from tutor.models import Tutor
from booking.models import Booking
from booking.forms import BookingForm

# Create your views here.
def tutor(request):
    tutors = Tutor.objects.all()
    return render(request, "tutor.html", {"tutors": tutors})


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

            # TODO: melhorar validacao
            booking = Booking.objects.filter(tutor_id=tutor_id, booking_date=booking_date, booking_time=booking_time).first()

            if booking:
                messages.error(request, 'Este tutor ja tem agendado este horario.')

            else:
                form.save()
                messages.success(request, 'Seu booking foi agendado com sucesso.')
                return redirect('index')
            
    else:
        form = BookingForm()

    tutor = Tutor.objects.filter(id=tutor_id).first()    
    return render(request, "tutor_detail.html", {"form": form,"tutor": tutor, "tutor_id": tutor_id })
