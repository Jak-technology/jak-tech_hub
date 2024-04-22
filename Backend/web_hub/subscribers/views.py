from rest_framework import generics, status
from rest_framework.response import Response

from .models import Subscriber
from .serializers import SubscriberSerializer
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class CreateSubscriberAPIView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def post(self, request):
        mutable_data = request.data.copy()
        mutable_data['active'] = True
        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            try:
                serializer.save()
                html_message = render_to_string('content/email.html')
                message = EmailMultiAlternatives(
                    subject="Keeping Up With Jak Technologies",
                    to=[mutable_data.get('email')],
                    from_email=settings.EMAIL_HOST_USER,
                )
                send_mail(
                    subject=,
                    message=f"Hello there!\nThank you for signing up to our Newsletter, you shall be among the first to know about all recent happenings and updates inside of Jak Technologies\nStay put, and have a good day👌",

                    fail_silently=False
                )
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)