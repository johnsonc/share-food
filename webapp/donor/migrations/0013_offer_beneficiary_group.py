# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0007_auto_20150514_1453'),
        ('donor', '0012_remove_offer_beneficiary_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='beneficiary_group',
            field=models.ManyToManyField(to='beneficiary.BeneficiaryGroup', verbose_name='Beneficiary group'),
            preserve_default=True,
        ),
    ]
