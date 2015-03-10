# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0002_auto_20150303_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(upload_to=b'/Users/anastasia/Work/ENSTA/PA/dev/tasdurab/infos/static/infos/images/'),
            preserve_default=True,
        ),
    ]
