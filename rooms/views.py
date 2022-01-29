from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Material, Publication, Room
from profiles.models import UserProfile
from .forms import CreateRoomForm, AddMaterialForm, AddPublicationForm, AddCategoryForm
from django.db import models


def dashboard(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except:
        if request.user.is_authenticated:
            return redirect('profiles:profile')
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'rooms/dashboard.html', context=context)


@login_required
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


def detail_room(request, id):
    room = Room.objects.get(id=id)
    materials = Material.objects.filter(room__id=id, publication=None)
    publications = Publication.objects.filter(room__id=id)
    context = {
        'room': room,
        'materials': materials,
        'publications': publications,
    }
    return render(request, 'rooms/detail.html', context=context)


@login_required
def add_material(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = AddMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.room = room
            form.filename = request.FILES['material']
            form.save()
            return redirect('rooms:detail', id)
    form = AddMaterialForm()
    context = {
        'form': form,
        'room': room,
    }

    return render(request, 'rooms/add_material.html', context=context)


@login_required
def add_publication(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = AddPublicationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.room = room
            form.save()
            return redirect('rooms:detail', id)

    form = AddPublicationForm()
    context = {
        'form': form,
        'room': room,
    }

    return render(request, 'rooms/add_publication.html', context=context)


def list_publications(request, room_id, id):
    room = Room.objects.get(id=room_id)
    publication = Publication.objects.get(id=id)
    materials = Material.objects.filter(publication=id)
    context = {
        'room': room,
        'publication': publication,
        'materials': materials,
    }
    return render(request, 'rooms/publication.html', context=context)


@login_required
def create_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.creator = request.user
            form.save()
            return redirect('rooms:create')
    form = AddCategoryForm()
    context = {
        'form': form
    }

    return render(request, 'rooms/create_category.html', context=context)
