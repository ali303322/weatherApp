# wrs/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('', views.home_view, name='home'),  # Home page
    path('weather/', views.weather_view, name='weather'),  # Home page
    path('recommendations/', views.recommendations_view, name='recommendations'),  # Recommendations page
    path('', auth_views.LoginView.as_view(), name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




