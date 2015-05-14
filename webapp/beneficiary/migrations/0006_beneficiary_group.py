# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0005_remove_beneficiary_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='group',
            field=models.ForeignKey(related_name='beneficiaries', blank=True, to='beneficiary.BeneficiaryGroup', null=True),
            preserve_default=True,
        ),
    ]
