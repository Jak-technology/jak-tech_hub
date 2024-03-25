from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Services
from .email_utils import send_email
from .serializers import ServicesSerializer
from django.core.mail import send_mail
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
                email = self.request.data.get('email')
                first_name = self.request.data.get('first_name')
                second_name = self.request.data.get('second_name')
                company_name = self.request.data.get('company_name')
                message = f"""Hello {first_name} {second_name}, Thank you for reaching out to us.\nWe at Jak Technologies have recieved your email regarding {request.data.get('service_requested')} services needed and we eager to get working with you\n"""

                #send email to user
                send_mail(
                    f"Jak Technologies - {company_name}""", #title
                    message, #message
                    settings.EMAIL_HOST_USER, #sender if not available, considered the default or configured sender
                    [email]
                    fail_silently=False
                )
                serializer.save()
                print(serializer.data)
                return Response(serializer.data)
            else:
                return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

        # serializer = self.get_serializer(data=self.request.data)