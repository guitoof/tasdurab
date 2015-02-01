# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            },
            bases=(models.Model,),
        ),
    ]
