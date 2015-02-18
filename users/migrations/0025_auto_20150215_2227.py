# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20150215_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='building',
            field=models.ForeignKey(default=1, to='housing.Building', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(default=1, to='housing.Room', null=True),
            preserve_default=True,
        ),
    ]
