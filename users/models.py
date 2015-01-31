from django.db import models

# Create your models here.

class Housing(models.Model):

    building = models.CharField(max_length=2)
    room = models.IntegerField()

class User(models.Model):

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    housing = models.ForeignKey(Housing)
