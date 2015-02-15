# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20150215_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room',
            field=models.ForeignKey(to='housing.Room', null=True),
            preserve_default=True,
        ),
    ]
