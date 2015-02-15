# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20150215_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=255, null=True, verbose_name=b'Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'T\xc3\xa9l\xc3\xa9phone'),
            preserve_default=True,
        ),
    ]
