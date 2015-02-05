# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20150205_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'Nom')),
            ],
            options={
                'verbose_name': 'Groupe',
                'verbose_name_plural': 'Groupe',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='graduation_year',
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, to='users.Group'),
            preserve_default=True,
        ),
    ]
