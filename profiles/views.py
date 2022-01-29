from django.shortcuts import render, redirect

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
            return redirect('rooms:dashboard')
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
            return redirect('rooms:dashboard')
    form = UserProfileForm()

    context = {
        'form': form
    }

    return render(request, 'profiles/profile.html', context=context)
