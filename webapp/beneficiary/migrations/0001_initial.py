# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_meals', models.PositiveIntegerField()),
                ('frozen_capacity', models.PositiveIntegerField()),
                ('refrigerated_capacity', models.PositiveIntegerField()),
                ('drystorage_capacity', models.PositiveIntegerField()),
                ('food_category', models.PositiveIntegerField()),
                ('dont_accept', models.PositiveIntegerField()),
                ('accept_meat_issue', models.PositiveSmallIntegerField()),
                ('accept_rel_issue', models.PositiveSmallIntegerField()),
                ('preference_info', models.TextField()),
                ('last_delivery', models.DateField()),
            ],
            options={
                'verbose_name': 'Beneficiary',
                'verbose_name_plural': 'Beneficiaries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BeneficiaryGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeliveryTimeWindows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_of_week', models.CharField(max_length=3, choices=[(b'Mon', 'Monday'), (b'Tue', 'Tuesday'), (b'Wed', 'Wednesday'), (b'Thu', 'Thursday'), (b'Fri', 'Friday'), (b'Sat', 'Saturday'), (b'Sun', 'Sunday')])),
                ('time_from', models.TimeField()),
                ('time_to', models.TimeField()),
                ('beneficiary', models.ForeignKey(related_name='deliveries', to='beneficiary.Beneficiary')),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='group',
            field=models.ForeignKey(blank=True, to='beneficiary.BeneficiaryGroup', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
