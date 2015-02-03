# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150202_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_superuser',
            new_name='is_admin',
        ),
    ]
