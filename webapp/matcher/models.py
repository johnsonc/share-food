from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    tel = models.CharField(max_length=255)
    user = models.ForeignKey(User)


class Routing(models.Model):
    driver_id = models.ForeignKey('Driver', to_field='id')
    date = models.DateField()
    id = models.AutoField(primary_key=True, unique=True)


class TemporalMatching(models.Model):
    offer_id = models.ForeignKey('Offer', to_field='id')
    beneficiary_id = models.ForeignKey('Beneficiary', to_field='id')
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()
    status = models.PositiveSmallIntegerField()


class VisitPoint(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    seq_num = models.PositiveSmallIntegerField()
    matched_id = models.ForeignKey('Matched', to_field='id')
    status = models.PositiveSmallIntegerField()
    donnor = models.BooleanField()


class Delivery(models.Model):
    routing_id = models.ForeignKey('Routing', to_field='id')
    visit_point = models.ForeignKey('VisitPoint', to_field='id')


class Matched(models.Model):
    offer_id = models.ForeignKey('Offer', to_field='id')
    beneficiary_id = models.ForeignKey('Beneficiary', to_field='id')
    driver_id = models.ForeignKey('Driver', to_field='id')
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()
    id = models.AutoField(primary_key=True, unique=True)