# import magic
import os
import smtplib
import ssl
from django.core.mail import EmailMessage
from django.conf import settings
from email.mime.base import MIMEBase
from email import encoders


# def send_mail_with_attachments(subject:str, message:str, from_email:str, recipient_list:list, attachment_path:str):
#     with open(attachment_path, 'rb') as file:
#         file_content = file.read()

#     mime_type = magic.from_buffer(file_content, mime=True)

#     #Extract filename from attachment path
#     file_name = os.path.basenae(attachment_path)
#     email = EmailMessage(subject, message, from_email, recipient_list)
#     email.attach(file_name, file_content, mime_type)

#     #send email
#     email.send()

def send_email(subject:str, message:str, recipient_list:list):
    smtp_port = settings.EMAIL_PORT
    smtp_server = settings.EMAIL_HOST
    sender_email = settings.EMAIL_HOST_USER

    # for person in recipient_list:
    #     message = message

    #     # make a MIME object to define parts of the email
    #     msg = MIMEMultipart()
    #     msg['From'] = sender_email
    #     msg['To'] = person
    #     msg['Subject'] = subject

    #     # Attach the body of the message
    #     msg.attach(MIMEText(message, 'plain'))

    #     #Define the file to attach
    #     # filename = attachment

    #     # Open the file in python as a binary
    #     # attachment = open(filename, 'rb')

    simple_email_context = ssl.create_default_context()

    try:
        print("connecting to email server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls(context=simple_email_context)
        TIE_server.login(sender_email, settings.EMAIL_HOST_PASSWORD)
        print("Connected to server")
        TIE_server.sendmail(sender_email, recipient_list, message)
    except Exception as e:
        print(e)

    finally:
        TIE_server.quit()