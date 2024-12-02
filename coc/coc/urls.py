from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('account/', include('django.contrib.auth.urls')),
    path('', include('videos.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('products/', include('products.urls')),
    path('services/', include('services.urls')),
    path('account/', include('allauth.urls')),
    path('home/', include('home.urls')),
    path('comments/', include('comments.urls')),
    path('notifications/', include('notifications.urls')),
    path('payments/', include('payments.urls')),
    path('search/', include('haystack.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header='Juice Haven Admin'
admin.site.site_title='Welcome to the Hub of Juice'
admin.site.index_title='Welcome to Juice Haven Admin System'

