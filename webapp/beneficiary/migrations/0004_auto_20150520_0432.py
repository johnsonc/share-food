# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionaries', '__first__'),
        ('beneficiary', '0003_remove_beneficiary_dont_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='dont_accept',
            field=models.ManyToManyField(related_name='ingredients_rejected_by_beneficiaries', to='dictionaries.FoodIngredients'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='food_category',
            field=models.ManyToManyField(related_name='food_accepted_by_beneficiaries', to='dictionaries.FoodCategory'),
            preserve_default=True,
        ),
    ]
