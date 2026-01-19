from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from users.models import CustomUser

@receiver(post_save, sender=CustomUser)
def welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:

        subject = "Welcome to HarvestBites Family! – A Dry Fruits Love 🍇"

        context = {
            "username": instance.username,
            "reset_link": "https://yourdomain.com/reset-password/",
            "account_link": "https://yourdomain.com/my-account/",
        }

        html_content = render_to_string(
            "emails/welcome.html",
            context
        )

        email = EmailMultiAlternatives(
            subject=subject,
            body="Welcome to Healthy Treats",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )

        email.attach_alternative(html_content, "text/html")
        email.send()
