from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    address = models.CharField(max_length=255)
    tel_1 = models.CharField(max_length=255)
    tel_2 = models.CharField(max_length=255, blank=True, null=True)
    default_mass_unit = models.CharField(max_length=5, choices=MASS_UNITS, default='kg') #Changed from positive integer
    location = models.PointField(blank=True, null=True)

    objects = models.GeoManager()

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __unicode__(self):
        return '%s profile' % self.user.username


def create_defaults(sender, instance, created, raw, using, update_fields, **kwargs):
    from django.contrib.gis.geos import Point

    if created:
        p = Profile(user=instance,
                    address="",
                    tel_1="",
                    tel_2="",
                    default_mass_unit='kg',
                    location=Point(-101.185547, 56.536854))
        p.save()

        o = Organization(name=Organization.DEFAULT_ORGANIZATION_NAME,
                            address='',
                            first_name='',
                            last_name='',
                            tel_1='',
                            tel_2='',
                            email='',
                            default_mass_unit='',
                            location=Point(-101.185547, 56.536854),
                            user=instance)
        o.save()

post_save.connect(create_defaults, sender=User)