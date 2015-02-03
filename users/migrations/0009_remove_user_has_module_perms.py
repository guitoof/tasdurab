# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_has_module_perms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='has_module_perms',
        ),
    ]
