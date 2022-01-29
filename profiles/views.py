from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm, UserProfileForm


def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('full sett')
    form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'UserProfile/create.html', context=context)


def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponse('full sett')
    form = UserProfileForm()

    context = {
        'form': form
    }

    return render(request, 'UserProfile/profile.html', context=context)
