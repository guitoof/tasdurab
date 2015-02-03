# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='title',
            field=models.CharField(default=b'', max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
