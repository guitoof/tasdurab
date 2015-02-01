from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from housing.models import Building, Room

class User(AbstractBaseUser):
    """
    Custom user class.
    """

    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    graduation_year = models.CharField(max_length=10)

    # Contact
    email = models.EmailField('email address')
    phone_number = models.CharField(max_length=255, default='')

    # Housing
    building = models.ForeignKey(Building)
    room = models.ForeignKey(Room)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    USERNAME_FIELD = 'username'


def getUserInfo(user):
    """ Calls getFirstName, getLastName, getEmail, which call
        a remote service to get that information.
        Their implementations are not important for this
        example.
    """
    user.username = getLogin(user.username)
    user.save()

# class User(Model):
#
#     username = CharField(max_length=255)
#     first_name = CharField(max_length=255)
#     last_name = CharField(max_length=255)
#     group = CharField(max_length=255)
#
#     # Contact
#     email = CharField(max_length=255)
#     phone_number = CharField(max_length=255, default='')
#
#     # Housing
#     building = ForeignKey(Building, default='')
#     room = ForeignKey(Room, default='')
#
#     def __unicode__(self):
#         return '%s %s' % (self.user.first_name, self.user.last_name)
#
#     def __str__(self):
#         return '%s %s' % (self.user.first_name, self.user.last_name)
