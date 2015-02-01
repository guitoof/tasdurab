from django.db import models

from housing.models import Building, Room

class Waster(models.Model):

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



def getUserInfo(user):
    """ Calls getFirstName, getLastName, getEmail, which call
        a remote service to get that information.
        Their implementations are not important for this
        example.
    """

    waster = Waster.objects.get(username=user.username)

    if not waster:
        print current_user
        current_user.username = user.username

    waster.save()
