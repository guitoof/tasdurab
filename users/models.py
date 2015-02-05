# -*- coding: utf-8 -*

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from housing.models import Building, Room


class Group(models.Model):

    title = models.CharField(max_length=20, verbose_name = 'Nom')

    class Meta:
        verbose_name = u'Groupe'
        verbose_name_plural = u'Groupe'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title



class UserManager(BaseUserManager):

    def get_by_natural_key(self, username):
        return User.objects.get(username=username)

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username,
                          password=password)

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

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default='', verbose_name = u'Prénom')
    last_name = models.CharField(max_length=255, default='', verbose_name = 'Nom')
    group = models.ForeignKey(Group, default=1, verbose_name = 'Groupe')

    # Contact
    email = models.EmailField(max_length=255, default='', verbose_name = 'Email')
    phone_number = models.CharField(max_length=255, default='', verbose_name = 'Téléphone')

    # Housing
    building = models.ForeignKey(Building)
    room = models.ForeignKey(Room)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)

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
