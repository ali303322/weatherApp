# wrs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather'),  # Home page
    path('recommendations/', views.recommendations_view, name='recommendations'),  # Recommendations page
]




