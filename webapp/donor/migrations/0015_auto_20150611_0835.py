# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0014_auto_20150610_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='user',
            field=models.OneToOneField(related_name='donor_group', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offer',
            name='donor',
            field=models.ForeignKey(related_name='donor_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 8, 35, 33, 304996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='time_to',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 8, 35, 33, 305027, tzinfo=utc)),
        ),
    ]
