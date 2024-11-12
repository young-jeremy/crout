from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('initiate/', views.payment_view, name='payment_view'),
    path('payments/callback/', views.payment_callback, name='payment_callback'),
    path('request-service/', views.request_service_view, name='request_service'),
    path('payments/callback/', views.payment_callback, name='payment_callback'),

]