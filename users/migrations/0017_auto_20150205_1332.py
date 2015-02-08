# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20150205_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='building',
            field=models.ForeignKey(default=0, to='housing.Building'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(default=0, to='housing.Room'),
            preserve_default=True,
        ),
    ]
