from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

from django.conf import settings  
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('' , include('accounts.urls')),
    path('home' , include('cart.urls')),
    path('admin/', admin.site.urls),
    path('api/' , include('api.urls')),
]


# urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 