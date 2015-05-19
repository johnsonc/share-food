# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0019_offer_packaging'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='packaging',
            field=models.ForeignKey(to='dictionaries.PackagingCategory'),
            preserve_default=True,
        ),
    ]
