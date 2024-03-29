from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Services
from .email_utils import send_email
from .serializers import ServicesSerializer
from django.conf import settings
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

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                email = serializer.data.get('email')
                first_name = serializer.data.get('first_name')
                second_name = serializer.data.get('second_name')
                company_name = serializer.data.get('company_name')
                files = self.request.FILES.get('file_uploaded')
                subject = f"Jak Technologies - {company_name}"""
                message = f"""Hello {first_name} {second_name}, Thank you for reaching out to us.\nWe at Jak Technologies have recieved your email regarding {request.data.get('service_requested')} services needed and we eager to get working with you\n"""
                try:
                    send_email(subject, message, [email])
                    return Response(serializer.data)
                except Exception as e:
                    return Response({f"message: Error sending email\n{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({f"message: Internal server Error\n{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)