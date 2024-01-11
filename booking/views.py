from django.shortcuts import render

# Create your views here.
def booking_list(request):
    return render(request, "booking/booking_list.html")

def booking_form(request):
    pass

def booking_delete(request):
    pass


