from rest_framework import serializers
from donor.models import Offer, Donor
from beneficiary.models import Beneficiary, BeneficiaryGroup
from matcher.models import TemporalMatching


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer

        
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor

class BeneficiaryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiaryGroup

        
class BeneficiarySerializer(serializers.ModelSerializer):
    bg_name =  BeneficiaryGroupSerializer()
    
    class Meta:
        model = Beneficiary
        fields = ('id', 'bg_name' ,'num_meals', 'frozen_capacity', 'drystorage_capacity', 'refrigerated_capacity', 'preference_info')
        

class TemporalMatchingSerializer(serializers.ModelSerializer):
    offer = OfferSerializer()
    beneficiary = BeneficiarySerializer()
    
    class Meta:
        model = TemporalMatching
        fields = ('id', 'offer' ,'beneficiary', 'status', 'quantity')
        
        