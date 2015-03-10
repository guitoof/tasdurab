# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Titre')),
                ('description', models.CharField(max_length=2048, verbose_name=b'Description')),
                ('image', models.ImageField(upload_to=b'/static/infos/infos')),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['pub_date'],
                'verbose_name': 'Info',
                'verbose_name_plural': 'Infos',
            },
            bases=(models.Model,),
        ),
    ]
