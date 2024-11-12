# from users.models import CustomUser
from django.conf import settings
from django.db import models
# from videos.models import Video
from videos.models import Comments


class CommentReply(models.Model):
    comment = models.ForeignKey(Comments, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_replies', blank=True)


class CommentReport(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='reports')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
