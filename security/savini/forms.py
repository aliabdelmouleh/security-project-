from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from .models import Contact


# - create/register a user 

class CreateUserForm(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if not password:
            raise ValidationError("Password cannot be empty.", code='password_empty')
        
        # Check if the password meets the minimum length requirement
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.", code='password_too_short')

        # Check if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.", code='password_no_uppercase')

        # Check if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.", code='password_no_digit')

        if not any(char in "!@#$%^&*()-_=+[]" for char in password):
            raise ValidationError("Password must contain at least one symbol.", code='password_no_symbol')

        return password


# - authenticate the user 

class loginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']










