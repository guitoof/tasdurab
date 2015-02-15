# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20150214_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='building',
            field=models.ForeignKey(to='housing.Building', null=True),
            preserve_default=True,
        ),
    ]
