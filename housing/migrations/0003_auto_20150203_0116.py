# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_auto_20150202_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
