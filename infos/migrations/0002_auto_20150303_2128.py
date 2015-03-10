# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(upload_to=b'/Users/guillaumediallo-mulliez/Work/ENSTA/3A/PA/TAsduRAB/dev/tasdurab/infos/static/infos/images/'),
            preserve_default=True,
        ),
    ]
