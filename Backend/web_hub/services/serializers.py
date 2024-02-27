from rest_framework import serializers
from .models import Services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['first_name', 'second_name', 'phone_number', 'email', 'company_name', 'country', 'preferred_contact', 'business_type', 'service_requested', 'image', 'message']
