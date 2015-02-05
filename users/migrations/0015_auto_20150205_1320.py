# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import housing.models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_auto_20150203_1721'),
        ('users', '0014_user_is_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='building',
            field=models.ForeignKey(default=1, to='housing.Building'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.ForeignKey(default=1, to='housing.Room'),
            preserve_default=True,
        ),
    ]
