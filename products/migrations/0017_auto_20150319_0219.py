# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 1, 19, 32, 641100, tzinfo=utc), verbose_name=b'Date de publication', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default=b'/Users/guillaumediallo-mulliez/Work/ENSTA/3A/PA/TAsduRAB/dev/tasdurab/products/static/categories/images/default.png', upload_to=b'/Users/guillaumediallo-mulliez/Work/ENSTA/3A/PA/TAsduRAB/dev/tasdurab/products/static/categories/images'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
