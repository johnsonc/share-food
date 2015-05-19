# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0017_auto_20150519_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='not_contain',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='packaging',
        ),
    ]
