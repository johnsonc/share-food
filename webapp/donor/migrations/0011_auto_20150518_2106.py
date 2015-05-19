# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0010_donnor_default_beneficiary_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donnor',
            name='default_beneficiary_group',
            field=models.ManyToManyField(to='beneficiary.BeneficiaryGroup', verbose_name='Beneficiary group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Delivery name'),
            preserve_default=True,
        ),
    ]
