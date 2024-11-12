from django.conf import settings
from django.db import models
from accounts.models import User

from videos.models import Content


class NotificationSettings(models.Model):
    # User associated with these settings
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Notification preferences for various actions
    email_on_password_change = models.BooleanField(default=True)
    email_on_video_upload = models.BooleanField(default=True)
    email_on_comment = models.BooleanField(default=True)
    email_on_newsletter = models.BooleanField(default=True)
    email_on_promotion = models.BooleanField(default=True)
    email_on_user_activity = models.BooleanField(default=True)
    send_notification_email = models.BooleanField(default=True)

    # Frequency of notifications
    notification_frequency_choices = [
        ('instant', 'Instant'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('never', 'Never'),
    ]
    notification_frequency = models.CharField(
        max_length=10,
        choices=notification_frequency_choices,
        default='instant'
    )

    # Additional settings related to notification delivery
    use_sms_notifications = models.BooleanField(default=False)
    sms_on_video_upload = models.BooleanField(default=False)
    sms_on_comment = models.BooleanField(default=False)

    # Can include a time frame for active notifications or quiet periods
    quiet_hours_start = models.TimeField(null=True, blank=True)
    quiet_hours_end = models.TimeField(null=True, blank=True)

    # Timestamps for when preferences were last modified
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Notification Settings for {self.user}'

    class Meta:
        verbose_name = 'Notification Setting'
        verbose_name_plural = 'Notification Settings'

    def should_notify(self, notification_type):
        """Method to check if a specific notification type is enabled."""
        if notification_type == 'password_change':
            return self.email_on_password_change
        elif notification_type == 'video_upload':
            return self.email_on_video_upload
        elif notification_type == 'comment':
            return self.email_on_comment
        elif notification_type == 'newsletter':
            return self.email_on_newsletter
        elif notification_type == 'promotion':
            return self.email_on_promotion
        elif notification_type == 'user_activity':
            return self.email_on_user_activity
        elif notification_type == 'send_notification_email':
            return self.send_notification_email
        return False  # Default is no notification


class Notifications(models.Model):
    notification_type = models.CharField(max_length=155, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    video = models.ForeignKey(Content, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Notification for {self.user} on {self.date_created}"




