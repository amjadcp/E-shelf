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

    def __str__(self):
        return f'{self.name}'


class Publication(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


def get_member_upload_to(instance, filename):
    new_filename = '{}'.format(filename.split('.')[0])
    if instance.publication.name != "noPublication":
        return "static/materials/{}/{}/{}".format(instance.room.name, instance.publication.name, new_filename)
    else:
        return "static/materials/{}/{}".format(instance.room.name, new_filename)


class Material(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, models.CASCADE)
    # default=Publication.objects.get(room=Room.objects.get(name='noRoom'))
    publication = models.ForeignKey(Publication, models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    material = models.FileField(upload_to=get_member_upload_to)

    def __str__(self):
        return f'{self.name}'
