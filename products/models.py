from django.db import models
from wasters.models import Waster

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Product(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    expiry_date = models.DateTimeField('expiry date')
    owner = models.ForeignKey(Waster)

    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
