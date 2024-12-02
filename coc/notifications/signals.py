# notifications/signals.py
from accounts.models import *
from accounts.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from videos.models import *  # Assuming this is your video model
from videos.models import Comments
# signals.py
from videos.models import Content
from .models import Notifications
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .utils import send_email_notification


@receiver(post_save, sender=User)
def notify_on_password_change(sender, instance, **kwargs):
    if instance.password:  # Password has been updated
        send_email_notification(
            instance,
            subject="Password Reset Successful",
            message="Your password has been reset successfully. If this was not you, please contact support immediately."
        )



@receiver(post_save, sender=Comments)
def comment_notification(sender, instance, created, **kwargs):
    if created:
        Notifications.objects.create(
            user=instance.video.uploader,  # The user who uploaded the video
            message=f"New comment on your video '{instance.video.title}': {instance.text}",
            notification_type='comment'
        )


@receiver(pre_save, sender=Content)
def update_video_notification(sender, instance, **kwargs):
    # For example, you might want to notify users when a video title is updated
    if instance.pk:
        old_video = Content.objects.get(pk=instance.pk)
        if old_video.title != instance.title:
            Notifications.objects.create(
                user=instance.uploader,
                message=f"Your video title has been updated to '{instance.title}'.",
                notification_type='video-update'
            )


def send_notification_email(instance, created, **kwargs):
    if created:
        # Only send the email if this is a new content entry
        # Customize the email sending logic as per your requirements
        subject = f"New content added: {instance.title}"
        message = f"Check out the new content titled '{instance.title}' in the category {instance.category}."
        recipient_list = ["jeremymayaka96@gmail.com"]
        send_mail(subject, message, "jeremymayaka96@gmail.com", recipient_list)


def notify(user, message, video=None):
    """Creates and saves a notification for a specific user."""
    notification = Notifications.objects.create(
        user=user,
        message=message,
        video=video
    )
    notification.save()


# Signal for creating notifications when a new comment is posted
@receiver(post_save, sender=Comments)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        notification = Notifications.objects.create(
            user=instance.video.uploader,  # The user who posted the video
            message=f"New comment on your video: {instance.text}",
            video=instance.video
        )
        notification.save()

# Signal for creating notifications when a new video is uploaded
@receiver(post_save, sender=Content)
def create_video_notification(sender, instance, created, **kwargs):
    if created:
        # Example: Notify all users about the new video
        for user in User.objects.all():
            Notifications.objects.create(
                user=user,
                message=f"New video uploaded: {instance.title}",
                video=instance
            )

# You can also add more signals for other types of notifications (e.g., followers, likes, etc.)
