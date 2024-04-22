from django.core.mail import send_mail
from django.conf import settings


send_mail(
    subject="Keeping Up With Jak Technologies",
    message=f"Hello there!\nThank you for signing up to our Newsletter, you shall be among the first to know about all recent happenings and updates inside of Jak Technologies\nStay put, and have a good day👌",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=['freddyjseg@gmail.com'],
    fail_silently=False
)