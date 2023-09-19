"""URL configuration for piano_store project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pianos.urls')),
    path('synths/', include('synths.urls')),
]
