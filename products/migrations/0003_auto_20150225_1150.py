# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150214_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['expiry_date'], 'verbose_name': 'Produit', 'verbose_name_plural': 'Produits'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='D\xe9j\xe0 Ouvert?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantit\xe9'),
            preserve_default=True,
        ),
    ]
