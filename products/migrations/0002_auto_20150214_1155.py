# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Cat\xe9gorie', 'verbose_name_plural': 'Cat\xe9gories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produit', 'verbose_name_plural': 'Produits'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name=b'Nom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name=b'Nom'),
            preserve_default=True,
        ),
    ]
