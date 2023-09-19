"""URL patterns for pianos."""

from django.urls import path
from . import views

app_name = 'pianos'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
]