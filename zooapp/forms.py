from django import forms
from .models import Registration,Booking
from django.contrib.auth import (
    authenticate,
    get_user_model
)
User = get_user_model()

class Signupform(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

class Loginform(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['email','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'