# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=255, db_index=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('graduation_year', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=75, verbose_name=b'email address')),
                ('phone_number', models.CharField(default=b'', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('building', models.ForeignKey(to='housing.Building')),
                ('room', models.ForeignKey(to='housing.Room')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
