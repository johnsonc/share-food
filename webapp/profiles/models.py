from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_lon = models.FloatField()
    address_lat = models.FloatField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tel_1 = models.CharField(max_length=255)
    tel_2 = models.CharField(max_length=255)
    email = models.EmailField()
    default_mass_unit = models.PositiveSmallIntegerField()
    donor = models.BooleanField()


class Profile(models.Model):
    TYPE = (
        ('D', 'Donor'),
        ('B', 'Beneficiary'),
        ('C', 'Driver')
    )
    user_type = models.CharField(max_length=1, choices=TYPE)
    organization = models.ForeignKey(Organization, null=True, blank=True)
    user = models.OneToOneField(User, related_name="profile")
    tel = models.CharField(max_length=255)


class Dictionary(models.Model):
    upper_dic_id = models.PositiveIntegerField()
    item_id = models.PositiveIntegerField()
    item_name = models.CharField(max_length=255)