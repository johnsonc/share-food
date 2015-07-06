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


def update_email(sender, instance, created, raw, using, update_fields, **kwargs):
    if not created or instance.user is not None:
        instance.user.email = instance.email
        instance.user.save()

post_save.connect(update_email, sender=Organization)


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

    try:
        profile = instance.profile
    except Exception:
        profile = Profile(user=instance,
                          default_mass_unit='kg',
                          donor=False,
                          beneficiary=False,
                          driver=False,
                          operator=False)
        instance.profile.save()

    from pinax.notifications.models import NoticeSetting, NoticeType
    notice_types = NoticeType.objects.all()
    for t in notice_types:
        ns = NoticeSetting(user=instance, notice_type=t, medium=0, send=True)
        ns.save()

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

    try:
        instance.email = instance.organization.email
    except Exception:
        instance.organization = Organization(name='Noname',
                                             address='',
                                             first_name='',
                                             last_name='',
                                             tel_1='',
                                             email='',
                                             default_mass_unit='kg',
                                             user=instance)
        instance.organization.save()


    instance.is_staff = True
    instance.save()

post_save.connect(create_defaults, sender=User)