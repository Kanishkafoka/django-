#form module - create form
#model authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    mobile_number = forms.CharField(max_length=25, help_text='Required. Enter your mobile number.')
    first_name = forms.CharField(max_length=30, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, help_text='Required. Enter your last name.')
    profile_image = forms.ImageField(required=False, help_text='Optional. Upload your profile image.')

    class Meta:
        model= User
        fields = ( 'first_name', 'last_name', 'mobile_number', 'email', 'username', 'password1', 'password2', 'profile_image')

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())