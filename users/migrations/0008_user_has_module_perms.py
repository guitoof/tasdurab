# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_module_perms',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
