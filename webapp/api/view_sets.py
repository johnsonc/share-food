from rest_framework import viewsets
from api.serializer import OfferSerializer, TemporalMatchingSerializer, BeneficiarySimpleSerializer,\
                            TemporalMatchingSimpleSerializer

from rest_framework import routers

#models
from donor.models import Offer
from matcher.models import TemporalMatching
from beneficiary.models import Beneficiary

import datetime

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
        status = self.request.data.get('status',-1)
        beneficiary_id = self.request.data.get('beneficiary',-1)
        if status == 2:
            print "process waiting"
            self.sendEmailToBeneficiary(beneficiary_id)
        elif status == 3:
            print "process confirmed"
        elif status == 4:
            print "process accepted"
        elif status == 5:
            print "process assigned"
        elif status == 6:
            print "process notified"
    
    def perform_update(self, serializer):
        self.statusChangeActions()
        serializer.save()
    
    def sendEmailToBeneficiary(self,beneficiary_id):
#        Sending email
        pass
    
    
router.register(r'temporal_matching_simple', TempMatchSimpleViewSet)



