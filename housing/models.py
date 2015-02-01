from django.db import models


class Building(models.Model):

    title = models.CharField(max_length=2)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return "%s" % self.title


class Room(models.Model):

    number = models.IntegerField()

    def __unicode__(self):
        return '%d' % self.number

    def __str__(self):
        return "%d" % self.number