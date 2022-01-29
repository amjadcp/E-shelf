from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Room
from profiles.models import UserProfile
from .forms import CreateRoomForm
from django.db import models


@login_required()
def dashboard(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except:
        return redirect('profiles:profile')
    rooms = Room.objects.filter(creator__email=request.user.email)
    context = {
        'rooms': rooms,
    }
    return render(request, 'rooms/dashboard.html', context=context)


def create_room(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.save()
            return redirect('rooms:dashboard')
    form = CreateRoomForm()
    context = {
        'form': form
    }

    return render(request, 'rooms/create.html', context=context)
