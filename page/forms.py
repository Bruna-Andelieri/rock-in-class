from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm

from user.models import User 

class AuthForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User 
        fields = ('email', 'password')
       
    def clean(self):
        cleaned_data = super(AuthForm, self).clean()


        email = cleaned_data['email']
        password = cleaned_data['password']

        # validation logic
        if not email:
            self.add_error("email", "Email should be informed")
        
        if not password:
            self.add_error("password", "Password should be informed")

        return cleaned_data
    

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True,validators=[EmailValidator(message='Please use a valid email')])
    password=forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ("name", "email", "password")
      
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]

        # validation logic
        if len(password) < 8:
            self.add_error("password", "Password must be at least 8 characters long")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data
    
    def save(self, commit=True):
        # Criar hash da senha usando make_password
        senha_hash = make_password(self.cleaned_data['password'])
        
        # Atualizar o valor do campo de senha no formulário
        self.instance.password = senha_hash

        # Salvar o formulário
        return super().save(commit)
