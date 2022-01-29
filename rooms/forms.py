from django.forms import ModelForm
from .models import Room, Material, Publication


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

class AddPublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'description')