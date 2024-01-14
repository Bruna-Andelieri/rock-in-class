from django.shortcuts import render


# Create your views here.
def page_index(request):
    return render(request, "index.html")


def page_tutor(request):
    return render(request, "tutor.html")


def page_lesson(request):
    return render(request, "lesson.html")


def page_contact(request):
    return render(request, "contact.html")

def page_about(request):
    return render(request, "about.html")

def page_booking(request):
    return render(request, "booking.html")
