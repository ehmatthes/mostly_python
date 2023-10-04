"""URL patterns for synths."""

from django.urls import path
from . import views

app_name = 'synths'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
]