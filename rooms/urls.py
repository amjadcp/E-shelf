from os import name
from django.urls import path
from .views import contrib_materials, contrib_publications, home, create_room, detail_room, add_material, add_publication, list_publications, create_category,contrib_rooms

app_name = 'rooms'

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_room, name='create'),
    path('<int:id>/', detail_room, name='detail'),
    path('<int:id>/add/', add_material, name='add-material'),
    path('<int:id>/add/publication/', add_publication, name='add-publication'),
    path('<int:room_id>/add/publication/<int:id>/',
         list_publications, name='publications'),
    path('category/create/', create_category, name='create-category'),
    path('contribrooms', contrib_rooms, name='contribrooms'),
    path('contribpublications', contrib_publications, name='contribpublications'),
    path('contribmaterials', contrib_materials, name='contribmaterials'),
]
