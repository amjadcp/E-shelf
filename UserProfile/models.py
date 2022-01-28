from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.


# class CustomUserManager(UserManager):
#     def create_user(self, email, username=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username, email, password, **extra_fields)


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
    profile_pic = models.ImageField(upload_to='static/profiles')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150, choices=QUALIFICATIONS)
    area_of_interest = models.CharField(max_length=150, choices=INTERESTS)
