from django.urls import path

from . import views

app_name='notifications'
urlpatterns = [
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications_settings/',views.notifications_settings,name='notifications_settings'),
    path('video_notifications/', views.create_video_notification, name='video_notifications'),
    path('send_sms/', views.send_sms_notification, name='send_sms_notification'),
    path('receive_sms/', views.receive_sms, name='receive_sms'),  # Webhook for incoming SMS
]
