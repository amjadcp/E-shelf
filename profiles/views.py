from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from rooms.models import Material, Publication, Room

from .forms import CustomUserCreationForm, UserProfileForm

from django.contrib.auth.decorators import login_required


def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('login')
    form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'registration/sign_up.html', context=context)


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('rooms:home')
    form = UserProfileForm()

    context = {
        'form': form
    }

    return render(request, 'profiles/create.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('rooms:home')
    form = UserProfileForm()

    context = {
        'form': form
    }

    return render(request, 'profiles/profile.html', context=context)

@login_required
def dashboard(request):
    user = request.user
    rooms = Room.objects.filter(creator=user)
    publications = Publication.objects.filter(creator=user)
    materials = Material.objects.filter(creator=user)
    context ={
        'user':user,
        'rooms':len(rooms),
        'publications':len(publications),
        'materials':len(materials),
    }
    
    return render(request, 'profiles/dashboard.html', context=context)


