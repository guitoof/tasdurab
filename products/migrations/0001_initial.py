# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('expiry_date', models.DateTimeField(verbose_name=b'expiry date')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.ForeignKey(to='products.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
