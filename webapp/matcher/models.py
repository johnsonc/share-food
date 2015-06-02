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
        return self.driver.user.username


class TemporalMatching(models.Model):
    STATUS_OPTS = (
        (1,_("pending")),
        (2,_("waiting")),
        (3,_("confirmed")),
        (4,_("accepted")),
        (5,_("assigned")),
        (6,_("notified"))
    )
    
    offer = models.ForeignKey('donor.Offer')
    beneficiary = models.ForeignKey('beneficiary.Beneficiary')
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()
    status = models.PositiveSmallIntegerField( max_length=1, choices = STATUS_OPTS )

    class Meta:
        verbose_name = _('Temporal match')
        verbose_name_plural = _('Temporal matchings')

    def __unicode__(self):
#        return '%s - %s @%s' (self.offer, self.beneficiary, str(self.date))
        return self.offer.name+" - "+self.beneficiary.group.name

class VisitPoint(models.Model):
    seq_num = models.PositiveSmallIntegerField()
    matched = models.ForeignKey('Matched', to_field='id')
    status = models.PositiveSmallIntegerField()
    donor = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Visit point')
        verbose_name_plural = _('Visit points')

    def __unicode__(self):
        return '%s' (self.seq_num)


class Delivery(models.Model):
    routing = models.ForeignKey(Routing)
    visit_point = models.ForeignKey(VisitPoint)

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Delivery points')

    def __unicode__(self):
        return 'deliver for %s' (self.routing)


class Matched(models.Model):
    offer = models.ForeignKey('donor.Offer')
    beneficiary = models.ForeignKey('beneficiary.Beneficiary')
    driver = models.ForeignKey(Driver)
    date = models.DateField()
    beneficiary_contact_person = models.CharField(max_length=255)
    quantity = models.FloatField()

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')

    def __unicode__(self):
        return '%s - %s @%s' (self.offer, self.beneficiary, str(self.date))
