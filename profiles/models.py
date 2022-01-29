from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .utils import get_user_profile_name


class User(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'


class UserProfile(models.Model):
    QUALIFICATIONS = (
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('Doctorate', 'Doctorate'),
        ('Post-graduate', 'Post-graduate')
    )

    INTERESTS = (
        ('Tech', 'Tech'),
        ('Non-Tech', 'Non-Tech'),
    )

    user = models.OneToOneRel(
        User, on_delete=models.CASCADE, to=None, field_name=None)
    profile_pic = models.ImageField(upload_to=get_user_profile_name)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150, choices=QUALIFICATIONS)
    area_of_interest = models.CharField(max_length=150, choices=INTERESTS)
