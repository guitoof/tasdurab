# -*- coding: utf-8 -*

from django.db import models
from users.models import User
from tasdurab import settings
import os


class Category(models.Model):

    title = models.CharField(max_length=255, verbose_name='Nom')
    image = models.ImageField(
        upload_to = os.path.join(settings.BASE_DIR, 'products/static/categories/images'),
        default = os.path.join(settings.BASE_DIR, 'products/static/categories/images/default.png')
        )

    class Meta:
        verbose_name = u'Catégorie'
        verbose_name_plural = u'Catégories'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(models.Model):

    category = models.ForeignKey(Category, verbose_name= u'Catégorie')
    title = models.CharField(max_length=255, verbose_name='Nom')
    description = models.CharField(max_length=2048, verbose_name= 'Description')
    expiry_date = models.DateField(verbose_name= u'Date de péremption')
    owner = models.ForeignKey(User)
    quantity = models.PositiveIntegerField(default=1, verbose_name= u'Quantité')
    is_opened = models.BooleanField(default= False, verbose_name= u'Déjà Ouvert?')


    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = u'Produit'
        verbose_name_plural = u'Produits'
        ordering = ['expiry_date']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
