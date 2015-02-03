from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from housing.models import Building, Room


class UserManager(BaseUserManager):

    def get_by_natural_key(self, username):
        return User.objects.get(username=username)

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_staff=True,
        user.is_admin=True,
        user.save()
        return user


class User(AbstractBaseUser):

    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    graduation_year = models.CharField(max_length=10, default='')

    # Contact
    email = models.EmailField('email address', max_length=255, default='')
    phone_number = models.CharField(max_length=255, default='')

    # Housing
    #building = models.ForeignKey(Building)
    #room = models.ForeignKey(Room)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')


    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin




# def getUserInfo(user):
#     """ Calls getFirstName, getLastName, getEmail, which call
#         a remote service to get that information.
#         Their implementations are not important for this
#         example.
#     """
#
#     current_user = User.objects.get(username=user.username)
#
#     # if (!current_user):
#     #     print current_user
#     #     current_user.username = user.username
#
#     current_user.save()

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
