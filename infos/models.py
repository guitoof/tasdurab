from django.db import models
from tasdurab import settings

import os

class Info(models.Model):

    title = models.CharField(max_length=255, verbose_name='Titre')
    description = models.TextField(max_length=2048, verbose_name= 'Description')
    image = models.ImageField(
        upload_to = os.path.join(settings.BASE_DIR, 'infos/static/infos/images/'),
    )
    pub_date = models.DateTimeField()

    class Meta:
        verbose_name = u'Info'
        verbose_name_plural = u'Infos'
        ordering = ['pub_date']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def getFileName(self):
        return self.image.url.split('/')[-1]
