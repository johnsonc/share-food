# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beneficiary', '0001_initial'),
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Delivery points',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matched',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('beneficiary_contact_person', models.CharField(max_length=255)),
                ('quantity', models.FloatField()),
                ('beneficiary', models.ForeignKey(to='beneficiary.Beneficiary')),
                ('driver', models.ForeignKey(to='matcher.Driver')),
                ('offer', models.ForeignKey(to='donor.Offer')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Routing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('driver', models.ForeignKey(to='matcher.Driver')),
            ],
            options={
                'verbose_name': 'Routing',
                'verbose_name_plural': 'Routings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemporalMatching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('beneficiary_contact_person', models.CharField(max_length=255)),
                ('quantity', models.FloatField()),
                ('status', models.PositiveSmallIntegerField()),
                ('beneficiary', models.ForeignKey(to='beneficiary.Beneficiary')),
                ('offer', models.ForeignKey(to='donor.Offer')),
            ],
            options={
                'verbose_name': 'Temporal match',
                'verbose_name_plural': 'Temporal matchings',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisitPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq_num', models.PositiveSmallIntegerField()),
                ('status', models.PositiveSmallIntegerField()),
                ('donor', models.BooleanField(default=True)),
                ('matched', models.ForeignKey(to='matcher.Matched')),
            ],
            options={
                'verbose_name': 'Visit point',
                'verbose_name_plural': 'Visit points',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='delivery',
            name='routing',
            field=models.ForeignKey(to='matcher.Routing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='delivery',
            name='visit_point',
            field=models.ForeignKey(to='matcher.VisitPoint'),
            preserve_default=True,
        ),
    ]
