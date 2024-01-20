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
        choices=TIME_OPTIONS,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'message']
        widgets = {
            'booking_date': forms.DateInput(attrs={'class':'datepicker', 'value': datetime.now().strftime("%d/%m/%Y")}),
            'booking_time': forms.Select(choices=TIME_OPTIONS),
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