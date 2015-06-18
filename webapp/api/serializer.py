from rest_framework import serializers
from donor.models import Offer, Donor
from beneficiary.models import Beneficiary, BeneficiaryGroup
from matcher.models import TemporalMatching, Driver
from django.contrib.auth.models import User
from profiles.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organization


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username',)


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
    group =  BeneficiaryGroupSerializer()
    
    class Meta:
        model = Beneficiary
        fields = ('id', 'group' ,'num_meals', 'frozen_capacity', 'drystorage_capacity', 'refrigerated_capacity', 'preference_info', 'last_delivery', 'user')
        

class TemporalMatchingSerializer(serializers.ModelSerializer):
    offer = OfferSerializer()
    beneficiary = BeneficiarySerializer()
    
    class Meta:
        model = TemporalMatching
        depth = 2
        fields = ('id', 'offer' ,'beneficiary', 'status', 'quantity','date','beneficiary_contact_person')
   

class TemporalMatchingSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TemporalMatching
        
        
class BeneficiarySimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beneficiary
   

class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Driver
        fields = ('id', 'user')
        
        