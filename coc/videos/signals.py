from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Content

@receiver(post_save, sender=Content)
def send_new_content_notification(sender, instance, created, **kwargs):
    if created:
        # You can add logic to send email or notifications here
        print(f"New content '{instance.title}' added to category '{instance.category.name}'")


