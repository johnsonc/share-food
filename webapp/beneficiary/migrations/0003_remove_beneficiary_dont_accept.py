# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0002_auto_20150520_0423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='dont_accept',
        ),
    ]
