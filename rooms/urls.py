from os import name
from django.urls import path
from .views import *

app_name = 'rooms'

urlpatterns = [
    path('', dash_board, name='dashboard')
]
