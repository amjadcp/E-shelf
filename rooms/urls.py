from os import name
from django.urls import path
from .views import dashboard, create_room, detail_room, add_material

app_name = 'rooms'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_room, name='create'),
    path('<int:id>/', detail_room, name='detail'),
    path('<int:id>/add/', add_material, name='add-material'),
]
