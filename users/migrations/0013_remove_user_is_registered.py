# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_is_registered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_registered',
        ),
    ]
