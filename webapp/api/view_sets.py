from rest_framework import viewsets
from api.serializer import OfferSerializer
from rest_framework import routers

#models
from donor.models import Offer

router = routers.DefaultRouter()

class OfferViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    
router.register(r'offer', OfferViewSet)