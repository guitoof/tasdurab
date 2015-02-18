# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20150215_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, verbose_name=b'Groupe', blank=True, to='users.Group'),
            preserve_default=True,
        ),
    ]
