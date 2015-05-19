# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0013_offer_beneficiary_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='food_category',
            field=models.ForeignKey(verbose_name='Food category', to='dictionaries.FoodCategory'),
            preserve_default=True,
        ),
    ]
