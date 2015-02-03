# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150202_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='building',
        ),
        migrations.RemoveField(
            model_name='user',
            name='room',
        ),
    ]
