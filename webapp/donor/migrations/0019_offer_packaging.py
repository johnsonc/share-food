# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '__first__'),
        ('donor', '0018_auto_20150519_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='packaging',
            field=models.ForeignKey(blank=True, to='dictionaries.PackagingCategory', null=True),
            preserve_default=True,
        ),
    ]
