from django.shortcuts import get_object_or_404, render

from tutor.models import Tutor
from booking.forms import BookingForm


# Create your views here.
def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, "tutor/tutor_list.html", {"tutors": tutors})


def tutor_detail(request, tutor_id):
    form = BookingForm()
    tutor = get_object_or_404(Tutor, id=tutor_id)

    return render(
        request,
        "tutor/tutor_detail.html",
        {
            "form": form,
            "tutor": tutor,
            "tutor_id": tutor_id,
        },
    )
