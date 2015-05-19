# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0011_auto_20150518_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='beneficiary_group',
        ),
    ]
