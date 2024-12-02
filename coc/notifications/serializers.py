# notifications/serializers.py
from rest_framework import serializers
from .models import VideoNotification

class VideoNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNotification
        fields = ['id', 'user', 'video_title', 'video_url', 'message', 'is_read', 'timestamp']
