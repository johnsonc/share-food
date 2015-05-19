# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0007_auto_20150514_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='organization_ptr',
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
