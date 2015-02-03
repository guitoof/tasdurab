# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_user_has_module_perms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Utilisateur', 'verbose_name_plural': 'Utilisateurs'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
