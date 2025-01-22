from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather'),  # Add a name for the URL pattern
]
