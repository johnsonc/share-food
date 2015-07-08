from rest_framework import viewsets
from api.serializer import OfferSerializer, TemporalMatchingSerializer, BeneficiarySimpleSerializer,\
                            TemporalMatchingSimpleSerializer, DriverSerializer, OrganizationSerializer,\
                            UserSerializer

from rest_framework import routers
from django.contrib.auth.models import User

#models
from donor.models import Offer
from matcher.models import TemporalMatching, Driver
from beneficiary.models import Beneficiary
from profiles.models import Organization

import datetime
import logging

logger = logging.getLogger(__name__)
router = routers.DefaultRouter()


class OfferViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    
router.register(r'offer', OfferViewSet)


class TemporalMatchingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TemporalMatchingSerializer
    queryset = TemporalMatching.objects.all()
    
    def get_queryset(self):
        if len(self.request.GET)>0:
            date = self.request.GET.get('date','')
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            
            year = date.split('-')[0]
            month  = date.split('-')[1]
            day = date.split('-')[2]
            
            return TemporalMatching.objects.filter(date__year = year, date__month = month, date__day = day)
        else:
            return self.queryset
    
router.register(r'temporal_matching', TemporalMatchingViewSet)

class BeneficiaryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = BeneficiarySimpleSerializer
    queryset = Beneficiary.objects.all()
    
router.register(r'beneficiary', BeneficiaryViewSet)


class TempMatchSimpleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TemporalMatchingSimpleSerializer
    queryset = TemporalMatching.objects.all()

    def statusChangeActions(self):

        status = self.request.data.get('status', -1)
        beneficiary_id = self.request.data.get('beneficiary', -1)
        driver_id = self.request.data.get('driver', -1)
        temp_matching_id = self.request.data.get('id', -1)
        
        if status == TemporalMatching.STATUS_WAITING:
            print "process waiting"
            self.send_email_to_beneficiary(beneficiary_id, temp_matching_id)
        elif status == TemporalMatching.STATUS_CONFIRMED:
            print "process confirmed"
        elif status == TemporalMatching.STATUS_ACCEPTED:
            print "process accepted"
        elif status == TemporalMatching.STATUS_ASSIGNED:
            print "process assigned"
            self.assign_driver(temp_matching_id, driver_id)
        elif status == TemporalMatching.STATUS_NOTIFIED:
            print "process notified"
            self.notify_all(temp_matching_id)
        elif status == TemporalMatching.STATUS_CANCELED:
            print "process cancel"
            self.cancel(temp_matching_id)

    def perform_update(self, serializer):
        self.statusChangeActions()
        serializer.save()

    def __send_notification(self, to, ntype, match):
        from django.conf import settings
        if "pinax.notifications" not in settings.INSTALLED_APPS:
            return
        from pinax.notifications import models as notification

        notification.send(to, ntype, {'match': match})

    def notify_beneficiaries_about_offer(self, temporal_matchings_ids=[]):
        matches = TemporalMatching.objects.filter(id__in=temporal_matchings_ids)
        for match in matches:
            self.__send_notification([match.beneficiary.user],
                                     "offer_to_beneficiary",
                                     match)

    def send_email_to_beneficiary(self, beneficiary_id, temporal_matching_id):
        """ TODO: remove after switching to notify_beneficiaries_about_offer"""
        if temporal_matching_id < 0:
            return

        match = TemporalMatching.objects.get(id=temporal_matching_id)
        self.__send_notification([match.beneficiary.user],
                                 "offer_to_beneficiary",
                                 match)

    def notify_all(self, temporal_matching_id):
        if temporal_matching_id < 0:
            return

        match = TemporalMatching.objects.get(id=temporal_matching_id)
        self.__send_notification([match.beneficiary.user],
                                 "transaction_notify",
                                 match)

    def assign_driver(self, temporal_matching_id, driver_id):
        if temporal_matching_id < 0 or driver_id < 0:
            return
        from matcher import matcher
        matcher.assign_driver_to_match(User.objects.get(id=driver_id),
                               TemporalMatching.objects.get(id=temporal_matching_id))

    def cancel(self, temporal_matching_id):
        print 'lets cance;'
        if temporal_matching_id < 0:
            return
        from matcher import matcher
        matcher.cancel_temporal_match(TemporalMatching.objects.get(id=temporal_matching_id))

router.register(r'temporal_matching_simple', TempMatchSimpleViewSet)


class DriverViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.filter(profile__driver=True)
    
router.register(r'drivers', DriverViewSet)


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    
    def get_queryset(self):
        if len(self.request.GET)>0:
            user = self.request.GET.get('user','')
            
            
            return Organization.objects.filter(user_id = user)
        else:
            return self.queryset
    
router.register(r'organization', OrganizationViewSet)


