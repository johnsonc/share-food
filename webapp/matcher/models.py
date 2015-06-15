from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


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

    STATUS = (
        ('p', _('Pending')),
        ('c', _('Confirmed')),
        ('a', _('Accepted')),
        ('w', _('Waiting'))
    )

    offer = models.ForeignKey('donor.Offer')
    beneficiary = models.ForeignKey('beneficiary.Beneficiary')
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()
    status = models.PositiveSmallIntegerField()
    hash = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _('Temporal match')
        verbose_name_plural = _('Temporal matchings')

    def send_offer(self):
        self.status = 'w'
        

    def offer_accepted(self, hash):
        if hash == self.hash:
            self.status = 'c'


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
