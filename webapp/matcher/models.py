from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from datetime import datetime
from django.db.models.signals import post_save


class Driver(models.Model):
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')

    def __unicode__(self):
        return self.user.username


class Routing(models.Model):
    driver = models.ForeignKey(Driver)
    date = models.DateField()

    class Meta:
        verbose_name = _('Routing')
        verbose_name_plural = _('Routings')

    def __unicode__(self):
        return str(self.date)


class TemporalMatching(models.Model):
    STATUS_PENDING = 1
    STATUS_WAITING = 2
    STATUS_CONFIRMED = 3
    STATUS_ACCEPTED = 4
    STATUS_ASSIGNED = 5
    STATUS_NOTIFIED = 6
    STATUS_EXPIRED = 7
    STATUS_CANCELED = 8

    STATUS_OPTS = (
        (STATUS_PENDING, _("pending")),
        (STATUS_WAITING, _("waiting")),
        (STATUS_CONFIRMED, _("confirmed")),
        (STATUS_ACCEPTED, _("accepted")),
        (STATUS_ASSIGNED, _("assigned")),
        (STATUS_NOTIFIED, _("notified")),
        (STATUS_EXPIRED, _("expired")),
        (STATUS_CANCELED, _("canceled"))
    )
    
    offer = models.ForeignKey('donor.Offer')
    beneficiary = models.ForeignKey('beneficiary.Beneficiary')
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()
    status = models.PositiveSmallIntegerField(max_length=1, choices=STATUS_OPTS)
    driver = models.ForeignKey(User, null=True, blank=True, default=None)
    hash = models.IntegerField(blank=True, null=True)
    waiting_since = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('Temporal match')
        verbose_name_plural = _('Temporal matchings')

    def send_offer(self):
        self.status = TemporalMatching.STATUS_WAITING

    def offer_accepted(self, hash):
        if hash == self.hash:
            self.status = TemporalMatching.STATUS_ACCEPTED


def update_confirmed_date(sender, instance, created, raw, using, update_fields, **kwargs):
    if created or 'status' not in update_fields:
        return
    if instance.status == TemporalMatching.STATUS_WAITING:
        instance.waiting_since = datetime.now()
        instance.save()

post_save.connect(update_confirmed_date, sender=TemporalMatching)


class VisitPoint(models.Model):
    STATUS = (
        ('p', _('Pending')),
        ('c', _('Confirmed')),
    )

    seq_num = models.PositiveSmallIntegerField()
    matched = models.ForeignKey('Matched', to_field='id')
    status = models.CharField(max_length=1, choices=STATUS, default='p')
    donor = models.BooleanField(default=False)
    routing = models.ForeignKey('Routing', related_name='visitpoints', null=True, blank=True)

    class Meta:
        verbose_name = _('Visit point')
        verbose_name_plural = _('Visit points')
        ordering = ['seq_num']


    def __unicode__(self):
        if self.donor:
            return self.matched.offer.address
        else:
            return self.matched.beneficiary.user.organization.address


"""
class Delivery(models.Model):
    routing = models.ForeignKey(Routing)
    visit_point = models.ForeignKey(VisitPoint)

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Delivery points')

    def __unicode__(self):
        return 'deliver for %s' (self.routing)
"""


class Matched(models.Model):
    offer = models.ForeignKey('donor.Offer')
    beneficiary = models.ForeignKey('beneficiary.Beneficiary')
    driver = models.ForeignKey(Driver)
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()

    class Meta:
        verbose_name = _('Delivery schedule (Match)')
        verbose_name_plural = _('Delivery schedules (Matches)')
        permissions = (
            ('readonly', 'Can read matches'),
        )

    def __unicode__(self):
        return '%s' % str(self.date)
