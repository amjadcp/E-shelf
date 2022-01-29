from django.db import models
from profiles.models import User

# Create your models here.


class Category(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Room(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'


class Publication(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


def get_member_upload_to(instance, filename):
    instance.filename = filename
    print(instance.publication is None)
    if not instance.publication is None:
        return "static/materials/{}/{}/{}".format(instance.room.name, instance.publication.name, filename)
    else:
        return "static/materials/{}/{}".format(instance.room.name, filename)


class Material(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, models.CASCADE)
    publication = models.ForeignKey(
        Publication, models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    filename = models.CharField(max_length=150, blank=True, null=True)
    material = models.FileField(upload_to=get_member_upload_to)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
