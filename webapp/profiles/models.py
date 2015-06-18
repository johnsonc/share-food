from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from matcher.models import Driver

DAYS_OF_THE_WEEK = ((0, _('Monday')),
                    (1, _('Tuesday')),
                    (2, _('Wednesday')),
                    (3, _('Thursday')),
                    (4, _('Friday')),
                    (5, _('Saturday')),
                    (6, _('Sunday')))


class Organization(models.Model):
    DEFAULT_ORGANIZATION_NAME = 'Individual'

    MASS_UNITS = (
        ('kg', 'kg'),
        ('lb', 'lb')
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tel_1 = models.CharField(max_length=255)
    tel_2 = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    default_mass_unit = models.CharField(max_length=5, choices=MASS_UNITS, default='kg') #Changed from positive integer
    location = models.PointField(blank=True, null=True)

    user = models.OneToOneField(User, related_name="organization")

    objects = models.GeoManager()

    class Meta:
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __unicode__(self):
        return self.name


class Profile(models.Model):
    DEFAULT_ORGANIZATION_NAME = 'Individual'

    MASS_UNITS = (
        ('kg', 'kg'),
        ('lb', 'lb')
    )

    user = models.OneToOneField(User, related_name="profile")
    default_mass_unit = models.CharField(max_length=5, choices=MASS_UNITS, default='kg') #Changed from positive integer

    donor = models.BooleanField(default=False)
    beneficiary = models.BooleanField(default=False)
    driver = models.BooleanField(default=False)
    operator = models.BooleanField(default=False)

    objects = models.GeoManager()

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __unicode__(self):
        return '%s profile' % self.user.username


def create_defaults(sender, instance, created, raw, using, update_fields, **kwargs):
    if not created:
        return

    from django.contrib.auth.models import Permission, Group
    from django.contrib.contenttypes.models import ContentType
    profile = instance.profile

    if profile.donor:
        instance.groups = [Group.objects.get(name='Donor')]

    if profile.driver:
        instance.groups = [Group.objects.get(name='Driver')]

        driver = Driver(user=instance)
        driver.save()

    if profile.operator:
        instance.groups = [Group.objects.get(name='Operator')]

    if profile.beneficiary:
        instance.groups = [Group.objects.get(name='Beneficiary')]

        from beneficiary.models import Beneficiary
        beny = Beneficiary(
            num_meals=0,
            frozen_capacity=0,
            refrigerated_capacity=0,
            drystorage_capacity=0,
            user=instance
        )
        beny.save()
    instance.email = instance.organization.email
    instance.is_staff = True
    instance.save()

post_save.connect(create_defaults, sender=User)