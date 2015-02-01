from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=255)


class Product(models.Model):

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    expiry_date = models.DateTimeField('expiry date')
    owner = models.ForeignKey(User)

    pub_date = models.DateTimeField('date published')
