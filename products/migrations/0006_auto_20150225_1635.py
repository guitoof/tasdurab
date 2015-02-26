# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_is_opened'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='D\xe9j\xe0 Ouvert?'),
            preserve_default=True,
        ),
    ]
