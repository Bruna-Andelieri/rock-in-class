from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'message']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.Select(choices=[(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]),
            'message': forms.Textarea(attrs={'placeholder': 'Message here...'}),
            'student': forms.HiddenInput(),
            'tutor': forms.HiddenInput(),
        }
        labels = {
            "booking_date": "Date",
            "booking_time": "Time",
            "message": "Message"
        }



# forms.py


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']
 
        labels = {
            "username": "Username",
            "email": "Email",
        }


class DeleteBookingForm(forms.Form):
    delete = forms.BooleanField(
        required=True,
        widget=forms.HiddenInput,
        initial=True,
        label='Are you sure?'
    )