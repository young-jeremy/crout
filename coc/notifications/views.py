from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# views.py
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import messaging
from notifications.signals import notify
from twilio.rest import Client
# firebase_admin.initialize_app(cred)
from twilio.rest import messaging
from twilio.twiml.messaging_response import MessagingResponse
from videos.models import *
from videos.models import Comments
from videos.models import Content
# notifications/views.py
from django.shortcuts import render
from .models import EmailNotification
# notifications/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import VideoNotification
from .serializers import VideoNotificationSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def video_notifications_list(request):
    notifications = VideoNotification.objects.filter(user=request.user).order_by('-timestamp')
    serializer = VideoNotificationSerializer(notifications, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(VideoNotification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return JsonResponse({'message': 'Notification marked as read.'})



@login_required()
def email_notifications_list(request):
    email_notifications = EmailNotification.objects.all().order_by('-timestamp')
    total_emails = EmailNotification.objects.all()
    email_count = total_emails.count()
    # Fetch all notifications
    return render(request, 'notifications/email_notifications.html', {'email_notifications': email_notifications})



from .forms import NotificationSettingsForm
from .models import Notifications
from .utils import send_email_notification


def send_email_notification(user, subject, message):
    if not user or not user.email:
        raise ValueError("Invalid user or email.")

    # Save the notification details in the database
    EmailNotification.objects.create(user=user, subject=subject, message=message)

    # Send the email
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )


@csrf_exempt
def receive_sms(request):
    response = MessagingResponse()
    response.message("Thank you for reaching out! We'll get back to you soon.")
    return HttpResponse(str(response), content_type="application/xml")


def send_sms_notification(request):
    # Initialize Twilio client
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    # Parameters for the SMS
    to_phone_number = request.GET.get("to", "")  # Recipient's phone number
    message_body = request.GET.get("message", "Hello from Juice Haven!")  # Message body

    # Send SMS
    message = client.messages.create(
        body=message_body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to_phone_number
    )

    # Return success response
    return JsonResponse({"message_sid": message.sid, "status": message.status})


def notifications_settings(request):
    if request.method == 'POST':
        form = NotificationSettingsForm(request.POST)
        if form.is_valid():
            # Handle form data here; save preferences to the database, if needed.
            # Example: Saving to session for demonstration (you would typically save to a user model)
            request.session['email_notifications'] = form.cleaned_data['email_notifications']
            request.session['password_change_notifications'] = form.cleaned_data['password_change_notifications']
            request.session['weekly_newsletter'] = form.cleaned_data['weekly_newsletter']
            request.session['product_promotions'] = form.cleaned_data['product_promotions']
            messages.success(request, 'Your notification settings have been changed successfully')
    else:
        # Prepopulate the form with session or model data if available
        form = NotificationSettingsForm(initial={
            'email_notifications': request.session.get('email_notifications', True),
            'password_change_notifications': request.session.get('password_change_notifications', True),
            'weekly_newsletter': request.session.get('weekly_newsletter', True),
            'product_promotions': request.session.get('product_promotions', True),
        })
    return render(request, 'accounts/profile.html', {'form': form})


def video_notifications(request):
    video_notification = VideoNotification.objects.all()
    video_notifications_count = video_notification.count()
    template_name = 'notifications/video_notifications.html'
    return render(request, template_name, {'video_notification': video_notification})


def email_notification(request):
    email_notifications = Notifications.objects.filter(notification_type=request.user)
    template_name = 'notifications/email_notifications.html'
    return render(request, template_name, {'email_notifications': email_notifications})


def notification_view(request, video_id, account_id):
    total_notifications = Notifications.objects.all()
    notifications_count = total_notifications.count()
    template_name = 'notifications/notification_view.html'
    comment_notification = Comments.objects.get(id=video_id)
    video_notification = Content.objects.get(id=vieo_id)
    account_notification = User.objects.get(id=user.account_id.notification)
    return render(request, template_name)


@receiver(pre_save, sender=Content)
def update_video_notification(sender, instance, **kwargs):
    # For example, you might want to notify users when a video title is updated
    if instance.pk:
        old_video = Content.objects.get(pk=instance.pk)
        if old_video.title != instance.title:
            Notifications.objects.create(
                user=instance.uploader.video,
                message=f"Your video title has been updated to '{instance.title}'.",
                notification_type='video-update'
            )



def send_push_notification(token, title, message):
    message = messaging.Message(
        notification=messaging.Notifications(
            title=title,
            body=message,
        ),
        token=token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)


def send_notification(sender, recipient, message):
    notify.send(sender, recipient=recipient, verb='sent you a message', description=message)


# In views
def create_comment_notification(request, pk):
    comment = Comments.objects.get(id=pk)
    # After a comment is created
    send_notification(request.user, comment.user, 'You have a new comment on your post')


@login_required
def notifications_view(request):
    # Get all notifications for the logged-in user
    notifications = Notifications.objects.filter(user=request.user).order_by('-date_created')
    notifications_count = Notifications.objects.all().count()
    categorized_notifications = {
        'video': notifications.filter(notification_type='video'),
        'email': notifications.filter(notification_type='email'),
        'account': notifications.filter(notification_type='account'),
        'other': notifications.filter(notification_type='other'),
    }
    email_notifications = notifications.filter(notification_type='email')
    # Optionally, mark all notifications as read
    notifications.update(is_read=True)

    return render(request, 'notifications/all_notifications.html', {'notifications': notifications, 'categorized_notification':categorized_notifications})


from django.core.mail import send_mail
from django.contrib import messages


def send_notification_email(user_email):
    subject = 'New Notification'
    message = 'You have a new notification.'
    from_email = 'jeremymayaka96@gmail.com'

    try:
        send_mail(subject, message, from_email, [user_email])
    except Exception as e:
        print("Email send failed:", e)
        # Optionally log or show an error message
