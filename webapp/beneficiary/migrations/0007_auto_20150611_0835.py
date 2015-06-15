# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0006_auto_20150520_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='user',
            field=models.OneToOneField(related_name='beneficiary_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
