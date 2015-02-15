# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20150210_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, verbose_name=b'Groupe', to='users.Group', null=True),
            preserve_default=True,
        ),
    ]
