# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150202_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=255, verbose_name=b'email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='graduation_year',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
