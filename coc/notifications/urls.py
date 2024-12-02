from django.urls import path

from . import views

app_name='notifications'
urlpatterns = [
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications_settings/',views.notifications_settings,name='notifications_settings'),
   # path('video_notifications/', views.create_video_notification, name='video_notifications'),
    path('send_sms/', views.send_sms_notification, name='send_sms_notification'),
    path('receive_sms/', views.receive_sms, name='receive_sms'),  # Webhook for incoming SMS
    path('email_notifications/', views.email_notification, name='email_notifications'),
    path('video_notifications/', views.video_notifications, name='video_notifications_list'),
    path('mark_as_read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
]
