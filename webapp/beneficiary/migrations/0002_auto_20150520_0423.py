# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='food_category',
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='drystorage_capacity',
            field=models.PositiveIntegerField(verbose_name='dry storage'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='frozen_capacity',
            field=models.PositiveIntegerField(verbose_name='frozen'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='num_meals',
            field=models.PositiveIntegerField(verbose_name='Number of meals served every day'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='refrigerated_capacity',
            field=models.PositiveIntegerField(verbose_name='refrigerated'),
            preserve_default=True,
        ),
    ]
