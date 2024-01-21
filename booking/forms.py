from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Booking

TIME_OPTIONS = [(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]
CHOICES = (
      (1, 'Orange'),
      (2, 'Mango'),
      (3, 'Strawberries'),
      (4, 'Grapes'),
      
  )
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