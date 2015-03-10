# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150226_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=b'/Users/anastasia/Work/ENSTA/PA/dev/tasdurab/products/static/categories/images/default.png', upload_to=b'/Users/anastasia/Work/ENSTA/PA/dev/tasdurab/products/static/categories/images'),
            preserve_default=True,
        ),
    ]
