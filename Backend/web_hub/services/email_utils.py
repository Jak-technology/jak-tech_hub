import os
import smtplib
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework.response import Response
from email.message import EmailMessage


def send_email(subject:str, body:str, recipients:list):
    try:
        for person in recipients:
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = person
            msg.set_content(body)
            with smtplib.SMTP_SSL(settings.EMAIL_HOST, setting.EMAIL_PORT) as smtp:
                smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                smtp.send_message(msg)
    except Exception as e:
        print({"Error sending email: ": e})