from django.urls import path
from .views import create_user, create_profile, profile, dashboard

app_name = 'profiles'

urlpatterns = [
    path('create/', create_profile, name='profile'),
    path('profile/', profile, name='create'),
    path('dashboard', dashboard, name='dashboard'),
]
