from django.urls import path
from .views import create_user, create_profile

app_name = 'profiles'

urlpatterns = [
    path('profile/', create_profile, name='profile'),
]
