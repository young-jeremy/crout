from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blogs_home, name='blogs_home'),
    path('articles/', views.articles,name='articles_home'),
    path('blog_post/',views.blog_post,name='blog_post'),

]