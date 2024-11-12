from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_home, name='products_home'),
    path('about_product/', views.about_product, name='about_product'),
    path('all_products/', views.all_products, name='all_products'),
    path('popular_products/', views.popular_products, name='popular_products'),
    path('new_products/', views.new_products, name='new_products'),


]