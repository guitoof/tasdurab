# -*- coding: utf-8 -*

from django.db import models
from users.models import User


class Category(models.Model):

    title = models.CharField(max_length=255, verbose_name='Nom')

    class Meta:
        verbose_name = u'Catégorie'
        verbose_name_plural = u'Catégories'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255, verbose_name='Nom')
    description = models.CharField(max_length=2048)
    expiry_date = models.DateTimeField('expiry date')
    owner = models.ForeignKey(User)

    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = u'Produit'
        verbose_name_plural = u'Produits'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
