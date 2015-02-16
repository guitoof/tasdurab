# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_auto_20150203_1721'),
        ('users', '0027_auto_20150216_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='building',
            field=models.ForeignKey(default=1, to='housing.Building', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=255, null=True, verbose_name=b'Email'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, blank=True, to='users.Group', null=True, verbose_name=b'Groupe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='is_registered',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'T\xc3\xa9l\xc3\xa9phone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.ForeignKey(default=1, to='housing.Room', null=True),
            preserve_default=True,
        ),
    ]
