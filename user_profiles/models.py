from django.db.models import Model
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import ForeignKey

from django.contrib.auth.models import User


class Housing(Model):

    building = CharField(max_length=2)
    room = IntegerField()


class UserProfile(Model):

    user = ForeignKey(User)
    phone_number = CharField(max_length=255, default='')
    housing = ForeignKey(Housing, default='')
