# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0007_auto_20150514_1453'),
        ('donor', '0009_auto_20150518_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnor',
            name='default_beneficiary_group',
            field=models.ManyToManyField(to='beneficiary.BeneficiaryGroup'),
            preserve_default=True,
        ),
    ]
