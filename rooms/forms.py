from django.forms import ModelForm
from .models import Room, Material


class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = (
            'name',
            'category',
            'description'
        )


class AddMaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ('publication', 'name', 'description', 'material')
