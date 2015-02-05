# Forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Models
from users.models import User

# Fields
from django.forms import EmailInput

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
        fields = ['email', 'phone_number', 'group']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail3', 'placeholder': 'Coucou'}),
        }
