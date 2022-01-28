from django.urls import path
from .views import create_user, create_profile

app_name = 'UserProfile'

urlpatterns = [
    path('', create_user, name='create'),
    path('profile/', create_profile, name='profile'),
]
