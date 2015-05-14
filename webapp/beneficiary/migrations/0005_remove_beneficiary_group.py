# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0004_beneficiarygroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='group',
        ),
    ]
