# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beneficiary', '0008_auto_20150519_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='user',
            field=models.OneToOneField(related_name='beneficiary_profile', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
