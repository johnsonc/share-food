# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0006_donnor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donnor',
            name='default_beneficiary_group',
        ),
    ]
