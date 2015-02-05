# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20150205_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='building',
            field=models.ForeignKey(to='housing.Building'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(to='housing.Room'),
            preserve_default=True,
        ),
    ]
