# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20150514_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerrepetition',
            name='day_of_week',
            field=models.CharField(max_length=3, choices=[(b'Mon', 'Monday'), (b'Tue', 'Tuesday'), (b'Wed', 'Wednesday'), (b'Thu', 'Thursday'), (b'Fri', 'Friday'), (b'Sat', 'Saturday'), (b'Sun', 'Sunday')]),
            preserve_default=True,
        ),
    ]
