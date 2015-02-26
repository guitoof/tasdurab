# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20150216_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Pr\xe9nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=2, blank=True, to='users.Group', null=True, verbose_name=b'Promo'),
            preserve_default=True,
        ),
    ]
