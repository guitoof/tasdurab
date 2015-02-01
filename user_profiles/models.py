from django.db.models import Model
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import ForeignKey

from django.contrib.auth.models import User


class Housing(Model):

    building = CharField(max_length=2)
    room = IntegerField()

    def __unicode__(self):
        return '%s%d' % (self.building, self.room)

    def __str__(self):
        return "%s%d" % (self.building, self.room)


class UserProfile(Model):

    user = ForeignKey(User)
    phone_number = CharField(max_length=255, default='')
    housing = ForeignKey(Housing, default='')

    def __unicode__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
