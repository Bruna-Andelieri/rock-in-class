from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Booking

TIME_OPTIONS = [(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]

class BookingForm(forms.ModelForm):

    booking_time = forms.ChoiceField(
        required=True,
        choices=TIME_OPTIONS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    booking_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),)

    message = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={
            "rows":"3", 
            'class': 'form-control', 
            'placeholder': 'Message here...'}))


    def clean(self):
        current_date = datetime.now().date()
        current_time = datetime.now().time()

        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = datetime.strptime(cleaned_data.get('booking_time'), '%H:%M').time()

        if booking_date <= current_date and booking_time <= current_time:
            raise ValidationError('Booking should be greather than today')
        

        if Booking.objects.filter(booking_date=booking_date, booking_time=cleaned_data.get('booking_time')).exists():
            raise ValidationError("Tutor is not available this day.")
        
      

    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'message']
        widgets = {
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