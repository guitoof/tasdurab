# -*- coding: utf-8 -*

from django.db import models

class Building(models.Model):

    title = models.CharField(max_length=2, default='', verbose_name='Nom')

    class Meta:
        verbose_name = u'Bâtiment'
        verbose_name_plural = u'Bâtiments'

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return "%s" % self.title


class Room(models.Model):

    number = models.IntegerField(verbose_name=u'Numéro')

    class Meta:
        verbose_name = u'Chambre'
        verbose_name_plural = u'Chambres'

    def __unicode__(self):
        return '%s' % self.number

    def __str__(self):
        return "%s" % self.number
