from django import forms
from moviepy.editor import VideoFileClip

from .models import Category, Content
from .models import LiveStreamEvent
from .models import ModerationRequest, ShortVideo, Comments


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'



class VideoForm(forms.ModelForm):
    video_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Content
        fields = '__all__'


class VideoSearchForm(forms.Form):
    query = forms.CharField(label='Search Videos', max_length=100, required=False)


class ContentSubmissionForm(forms.Form):
    class Meta:
        model = Content
        fields = '__all__'


class ModerationRequestForm(forms.ModelForm):
    class Meta:
        model = ModerationRequest
        fields = ['user', 'video', 'is_approved', ]


class ShortVideoForm(forms.Form):
    video = forms.FileField()

    class Meta:
        model = ShortVideo
        fields = '__all__'

    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            # Get the user-specified video duration (default to 1 minute)
            desired_duration = self.cleaned_data.get('desired_duration', 60)

            # Use moviepy to trim the video to the desired duration
            clip = VideoFileClip(video.temporary_file_path())
            if clip.duration <= desired_duration:
                return video

            trimmed_clip = clip.subclip(0, desired_duration)
            trimmed_clip.write_videofile(video.temporary_file_path())
            return video


class ContentModerationForm(forms.Form):
    class Meta:
        model = Content
        fields = ['moderation']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']



class CommentEditForm(forms.Form):
    class Meta:
        model = Comments
        fields = ['text']


class LiveStreamEventForm(forms.ModelForm):
    class Meta:
        model = LiveStreamEvent
        fields = ['title', 'stream_key', 'start_time', 'description']
