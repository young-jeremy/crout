from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Channel, Subscription
from videos.models import Content


@login_required
def video_feed(request):
    subscriptions = Subscription.objects.filter(subscriber=request.user)
    channels = [subscription.channel for subscription in subscriptions]
    videos = Content.objects.filter(channel__in=channels).order_by('-uploaded_at')
    return render(request, 'video_feed.html', {'videos': videos})


@login_required
def subscriptions_view(request):
    # Get the current user's subscriptions
    subscriptions = Subscription.objects.filter(subscriber=request.user)
    is_subscribed = subscriptions.exists()


    # Get all channels the user is subscribed to
    subscribed_channel_ids = [subscription.channel.id for subscription in subscriptions]

    # Get all available channels (or those relevant for display)
    channels = Channel.objects.all()

    return render(
        request,
        'services/subscriptions.html',
        {
            'channels': channels,
            'subscribed_channel_ids': subscribed_channel_ids,
            'is_subscribed': is_subscribed
        }
    )


# View to subscribe to a channel
@login_required
def subscribe_view(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    if not Subscription.objects.filter(subscriber=request.user, channel=channel).exists():
        Subscription.objects.create(subscriber=request.user, channel=channel)
    return redirect('services:subscriptions')  # Redirect to the subscriptions page


# View to unsubscribe from a channel
@login_required
def unsubscribe_view(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)
    subscription = Subscription.objects.filter(subscriber=request.user, channel=channel).first()
    if subscription:
        subscription.delete()
    return redirect('services:subscriptions')


def services(request):
    template_name ='services/services.html'
    return render(request, template_name)