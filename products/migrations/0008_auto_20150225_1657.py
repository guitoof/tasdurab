# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150225_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_opened',
            field=models.BooleanField(default=False, verbose_name='D\xe9j\xe0 Ouvert?', choices=[(True, b'oui'), (False, b'non')]),
            preserve_default=True,
        ),
    ]
