# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0004_auto_20150520_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='accept_meat_issue',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='accept_rel_issue',
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='dont_accept',
            field=models.ManyToManyField(related_name='ingredients_rejected_by_beneficiaries', verbose_name="We don't accept food CONTAINING:", to='dictionaries.FoodIngredients'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='food_category',
            field=models.ManyToManyField(related_name='food_accepted_by_beneficiaries', verbose_name='We would like to receive:', to='dictionaries.FoodCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='preference_info',
            field=models.TextField(verbose_name='Additional info:'),
            preserve_default=True,
        ),
    ]
