# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0007_auto_20150514_1453'),
        ('donor', '0007_remove_donnor_default_beneficiary_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnor',
            name='default_beneficiary_group',
            field=models.ForeignKey(blank=True, to='beneficiary.BeneficiaryGroup', null=True),
            preserve_default=True,
        ),
    ]
