# -*- coding: utf-8 -*

# Forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Models
from users.models import User

# Fields
from django.forms import EmailInput, TextInput, Select

# Validation
from django.forms import ValidationError


# Utils
import re

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'



class UserRegistrationForm(ModelForm):
    """
    A form that creates a user, for the app (is actually a registration form since the user is actually already logged in from cascad)
    """

    class Meta:
        model = User
        fields = ['group', 'email', 'phone_number', 'building', 'room']
        widgets = {
            'group': Select(attrs={'class': 'form-control', 'id': 'inputGroup'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'prenom.nom@ensta-paristech.fr'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'inputPhoneNumber', 'placeholder': '06******'}),
            'building': Select(attrs={'class': 'form-control', 'id': 'inputBuilding'}),
            'room': Select(attrs={'class': 'form-control', 'id': 'inputRoom'}),
        }


    def clean_email(self):
        valid_format = re.compile(r'^[\w-]+(?:\.[\w-]+)*@(ensta-paristech.fr)$')
        if not valid_format.match(self.cleaned_data.get('email')):
            raise ValidationError('Format invalide: utilise un email de la forme prenom.nom@ensta-paristech.fr' )
        return self.cleaned_data.get('email')

    def clean_phone_number(self):
        valid_format = re.compile(r'^0[0-9]([ .-]?[0-9]{2}){4}$')
        if not valid_format.match(self.cleaned_data.get('phone_number')):
            raise ValidationError('Format invalide: utilise un numéro de la forme 06********')
        return self.cleaned_data.get('phone_number')
