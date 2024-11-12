from django.shortcuts import redirect

from .models import UserProfile

def channel_verified_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            try:
                channel = user.profile.channel_name
                if channel == 'verified':
                    return view_func(request, *args, **kwargs)
            except UserProfile.DoesNotExist:
                pass

        return redirect('videos:home')  # You can redirect to a different URL or show an error message
    return _wrapped_view
