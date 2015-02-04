# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150203_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_registered',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
