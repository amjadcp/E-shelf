from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'profile_pic',
            'first_name',
            'last_name',
            'qualification',
            'area_of_interest',
        )
