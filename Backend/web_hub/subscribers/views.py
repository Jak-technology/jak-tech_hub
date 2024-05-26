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
                html_message = render_to_string("email.html")
                plain_message = strip_tags(html_message)
                try:
                    message = EmailMultiAlternatives(
                        subject="Keeping Up With Jak Technologies",
                        body=plain_message,
                        to=["freddyjseg@gmail.com"],
                        from_email=settings.EMAIL_HOST_USER,
                    )
                    message.attach_alternative(html_message, 'text/html')
                    message.send()
                except Exception as e:
                    return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)