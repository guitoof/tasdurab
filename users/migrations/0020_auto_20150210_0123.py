# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20150205_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Groupe', 'verbose_name_plural': 'Groupes'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=255, verbose_name=b'Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=b'', max_length=255, verbose_name='Pr\xe9nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, verbose_name=b'Groupe', to='users.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'T\xc3\xa9l\xc3\xa9phone'),
            preserve_default=True,
        ),
    ]
