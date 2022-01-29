from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from profiles.views import create_user

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='landing_page.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('rooms/', include('rooms.urls', namespace='rooms')),
    path('login/', LoginView.as_view(), name='login'),
    path('sign-up/', create_user, name='sign-up'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
