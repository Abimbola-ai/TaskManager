from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Required, Enter a valid email address. ")

class SignInForm(AuthenticationForm):
    pass