# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0038_auto_20150618_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='time_from',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='time_to',
        ),
        migrations.AddField(
            model_name='offer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 19, 5, 46, 51, 983664, tzinfo=utc), verbose_name='Offer available at'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='valid_to',
            field=models.DateField(default=datetime.datetime(2015, 6, 20, 5, 46, 51, 983693, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='day_freq',
            field=models.PositiveSmallIntegerField(verbose_name='Day frequency', choices=[(0, 'Every week'), (1, '1st in the month'), (2, '2nd in the month'), (3, '3rd in the month'), (4, '4th in the month')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerrepetition',
            name='offer',
            field=models.ForeignKey(related_name='repetitions', to='donor.Offer'),
            preserve_default=True,
        ),
    ]
