from django.contrib import admin
from .models import Category, Room, Publication, Material

admin.site.register(Room)
admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Material)
