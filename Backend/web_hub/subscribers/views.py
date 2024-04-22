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
        print("We got here 1")
        mutable_data['active'] = True
        print(2)
        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            try:
                serializer.save()
                print(3)
                html_message = render_to_string("email.html")
                print("html_message")
                plain_message = strip_tags(html_message)
                print("strip_tags")
                try:
                    message = EmailMultiAlternatives(
                        subject="Keeping Up With Jak Technologies",
                        body=plain_message,
                        to=[mutable_data.get('email')],
                        from_email=settings.EMAIL_HOST_USER,
                    )
                    print("here before email sent")
                    message.attach_alternative(html_message, 'text/html')
                    print("here before email sent22222")
                    message.send()
                    print("sent email")
                except Exception as e:
                    print(str(e))
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)