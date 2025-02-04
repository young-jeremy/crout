import logging

from django.conf import settings
# from users.models import CustomUser
# from .utils import get_video_duration
# from like_system.models import LikesTarget
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

logger = logging.getLogger(__name__)


CATEGORY_CHOICES = [
    ('MUSIC', 'music'),
    ('SERMON', 'sermon'),
    ('PREACHING', 'preaching'),
    ('BIBLE_STUDY', 'bible_study'),
    ('PRAISE_AND_WORSHIP', 'praise_and_worship'),
    ('ALL_TESTIMONIES', 'all_testimonies'),
    ('BIBLE_DISCUSSIONS', 'bible_discussions'),
    ('EVANGELISM', 'evangelism'),
    ('STREET_PRAISE_AND_WORSHIP_MUSIC_AND_PREACHING', 'street_worship_music'),
    ('GOSPEL_MADE_FOR_KIDS', 'gospel_made_for_kids'),

]

MODERATION_CHOICES = [
    ('PENDING', 'pending'),
    ('APPROVED', 'approved'),
    ('REJECTED', 'rejected'),
]

PRIVACY_CHOICES = [
        ('PUBLIC', 'public'),
        ('PRIVATE', 'private'),
        ('COMMUNITY', 'community'),
        ('MADE_FOR_KIDS', 'made_for_kids'),
    ]





class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='contents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='static/imag/sa.jpg')
    audience = models.BooleanField(default=False)
    path = models.FileField(upload_to='videos/', null=True, verbose_name="")
    recording_date_and_location = models.DateTimeField(blank=True, null=True)
    language_and_captions_certification = models.BooleanField(default=False)
    license = models.BooleanField(default=False)
   # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    keywords = models.CharField(max_length=100, null=True, blank=True)

    views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=100, null=True, blank=True, choices=MODERATION_CHOICES, default='PENDING')
    privacy = models.CharField(max_length=100, choices=PRIVACY_CHOICES, default='PUBLIC')
    is_blocked = models.BooleanField(default=False)
    duration = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    promoted = models.BooleanField(default=False)
    url = models.URLField(default='https://example.com')

    def __str__(self):
        # Use a more explicit check and ensure it returns a string always
        return self.title if self.title else "Content with No Title"

    def get_absolute_url(self):
        return reverse('videos:video_details', kwargs={'video_id': self.id})


class ShortVideo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='short_videos/')
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title




class Moderation(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=MODERATION_CHOICES, )
    # video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()



class Privacy(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=100, choices=PRIVACY_CHOICES,)
    # video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.level


class Playlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # The user who owns the playlist
    name = models.CharField(max_length=100)
    videos = models.ManyToManyField('Content')  # Assuming you have a Video model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ModerationRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Content, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s request for {self.video.title}"


class ContentGuidelines(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class LikedVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Content, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} liked {self.video.title}'


class FavoriteVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Content, on_delete=models.CASCADE)  # Assuming you have a Video model
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s  favorite videos:  {self.video.title}"




class UploadedVideo(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class VideoView(models.Model):
    video = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Share(models.Model):
    video = models.ForeignKey(Content, on_delete=models.CASCADE, blank=True, null=True)
    number_of_times_shared = models.PositiveIntegerField(default=0)
    shared = models.BooleanField(default=False)


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    video = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(validators=[MinLengthValidator(150)], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments')
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_comments')
    parent = models.ForeignKey('self', validators=[MinLengthValidator(150)], on_delete=models.CASCADE, blank=True, null=True)

    def get_total_likes(self):
        return self.likes.users.count()

    def total_dislikes(self):
        return self.dislikes.users.count()

    def __str__(self):
        return f'comment by {self.user} on {self.created_at}'[:30]

    class Meta:
        ordering = ['created_at']

class VideoLikes(models.Model):
    video = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.video.title}"


class VideoHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Content, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-watched_at']  # Order by the timestamp in descending order

    def __str__(self):
        return f"{self.user.username} watched {self.video.title}"


class LiveStreamEvent(models.Model):
    title = models.CharField(max_length=200)
    stream_key = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    description = models.TextField()


class WatchLater(models.Model):
    video = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"


class Subscribe(models.Model):
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class VideoQueue:
    def __init__(self):
        self.queue = []

    def add_video(self, video_id):
        """Add a video to the queue."""
        self.queue.append(video_id)
        print(f"Video {video_id} added to the queue.")

    def remove_video(self, video_id):
        """Remove a specific video from the queue."""
        if video_id in self.queue:
            self.queue.remove(video_id)
            print(f"Video {video_id} removed from the queue.")
        else:
            print(f"Video {video_id} not found in the queue.")

    def clear_queue(self):
        """Clear all videos from the queue."""
        self.queue.clear()
        print("All videos have been removed from the queue.")

    def display_queue(self):
        """Display the current queue."""
        print("Current Video Queue:")
        for idx, video_id in enumerate(self.queue, start=1):
            print(f"{idx}. Video ID: {video_id}")
