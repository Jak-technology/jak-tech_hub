from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Services
from .serializers import ServicesSerializer
import json



@api_view(['GET'])
def get_choices(request):
    contact_choices = dict(Services._meta.get_field('preferred_contact').choices)
    service_choices = dict(Services._meta.get_field('service_requested').choices)
    business_type_choices = dict(Services._meta.get_field('business_type').choices)

    data = {
        'contact_choices': contact_choices,
        'service_choices': service_choices,
        'business_type_choices': business_type_choices,
    }

    return Response(data, status=status.HTTP_200_OK)


class ServicesListCreateView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    

    #def perform_create(self, serializer):
        #serializer.save()  # This method saves the new object to the database

    # Uncomment the following line if you want to allow only authenticated users to create services
    # permission_classes = [permissions.IsAuthenticated]

    # Override the 'create' method to handle POST requests
    #def create(self, request, *args, **kwargs):
        #return self.create(request, *args, **kwargs)