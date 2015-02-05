# Forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Models
from users.models import User

# Fields
from django.forms import EmailInput, TextInput, Select

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
        fields = ['email', 'phone_number', 'building', 'room']
        widgets = {
            # 'first_name': TextInput(attrs={'class': 'form-control', 'id': 'inputFirstName', 'disabled': True}),
            # 'last_name': TextInput(attrs={'class': 'form-control', 'id': 'inputLastName', 'disabled': True}),
            # 'group': Select(attrs={'class': 'form-control', 'id': 'inputGroup', 'disabled': True}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'id': 'inputPhoneNumber'}),
            'building': Select(attrs={'class': 'form-control', 'id': 'inputBuilding'}),
            'room': Select(attrs={'class': 'form-control', 'id': 'inputRoom'}),
        }


    def clean_phone_number(self):
        valid_format = re.compile(r'^0[0-9]([ .-]?[0-9]{2}){4}$')
        if not valid_format.match(self.cleaned_data.get('phone_format')):
            raise ValidationError("Format invalide (essaye avec 0612345678)")

        return self.cleaned_data
