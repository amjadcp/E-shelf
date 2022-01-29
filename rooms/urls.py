from os import name
from django.urls import path
from .views import dashboard, create_room

app_name = 'rooms'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_room, name='create'),
]
