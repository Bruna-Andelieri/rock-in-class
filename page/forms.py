from django import forms
from django.core.validators import EmailValidator

from user.models import User 

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', validators=[EmailValidator(message='Please use a valid email')])
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("name", "email", "password")
      
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data
