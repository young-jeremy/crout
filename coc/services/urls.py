from django.urls import path
from . import views

from django.urls import path
from . import views
app_name = 'services'




urlpatterns = [
    path('subscriptions/', views.subscriptions_view, name='subscriptions'),
    path('subscribe/<int:channel_id>/', views.subscribe_view, name='subscribe'),
    path('unsubscribe/<int:channel_id>/', views.unsubscribe_view, name='unsubscribe'),
    path('', views.services, name='services_home'),
]