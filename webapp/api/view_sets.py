from rest_framework import viewsets
from api.serializer import OfferSerializer, TemporalMatchingSerializer
from rest_framework import routers

#models
from donor.models import Offer
from matcher.models import TemporalMatching

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