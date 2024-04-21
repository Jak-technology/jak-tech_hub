from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPostComment
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=BlogPostComment)
def send_email_on_comment_creation(sender, instance, created, **kwargs):
    if created:
        subject = 'Your comment has been posted!'
        message = f'Dear {instance.author},\n\nYour comment on blog post "{instance.blogpost.title}" has been successfully posted.\n\nBest regards,\n[Your Name]'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)