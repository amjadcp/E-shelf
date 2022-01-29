from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='/login/')
def dash_board(request):
    email = request.user.email
    print(Room.objects.filter(creator__email=email))
    return render(request, 'dash.html')
