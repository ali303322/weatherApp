# wrs/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.weather_view, name='weather'),  # Home page
    path('recommendations/', views.recommendations_view, name='recommendations'),  # Recommendations page
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




