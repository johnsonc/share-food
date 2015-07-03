# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0019_remove_temporalmatching_confirmed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporalmatching',
            name='waiting_since',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
