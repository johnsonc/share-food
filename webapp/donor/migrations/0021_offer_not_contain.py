# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '__first__'),
        ('donor', '0020_auto_20150519_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='not_contain',
            field=models.ManyToManyField(to='dictionaries.FoodIngredients', null=True, blank=True),
            preserve_default=True,
        ),
    ]
