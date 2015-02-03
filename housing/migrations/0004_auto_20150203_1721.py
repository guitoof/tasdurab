# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_auto_20150203_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'verbose_name': 'B\xe2timent', 'verbose_name_plural': 'B\xe2timents'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Chambre', 'verbose_name_plural': 'Chambres'},
        ),
        migrations.AlterField(
            model_name='building',
            name='title',
            field=models.CharField(default=b'', max_length=2, verbose_name=b'Nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(verbose_name='Num\xe9ro'),
            preserve_default=True,
        ),
    ]
