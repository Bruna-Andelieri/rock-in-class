# forms.py
from django import forms
from .models import Booking

# forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'message']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(choices=[(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]),
            'student': forms.HiddenInput(),
            'tutor': forms.HiddenInput(),
        }
        labels = {
            "booking_date": "Date",
            "booking_time": "Time",
            "message": "Message"
        }
