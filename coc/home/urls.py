from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('juice_haven/', views.juice_haven, name='juice_haven'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('frequently_asked_questions/', views.frequently_asked_questions, name='frequently_asked_questions'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('portfolio_overview/', views.portfolio_overview, name='portfolio_overview'),
    path('portfolio_item/', views.portfolio_item, name='portfolio_item'),
    path('blog_post/', views.blog_post, name='blog_post'),
    path('blog_home/', views.blog_home, name='blog_home'),
    path('learn_more/', views.learn_more, name='learn_more'),
    path('pricing/', views.pricing, name='pricing'),


]