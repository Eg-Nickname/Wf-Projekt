from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm

from .models import Uczniowie, Obecnosci

from .forms import ObecnoscForm

def obecnosc_view(request):
    context={}
    obj = Uczniowie.objects.none()
    form = ObecnoscForm(request.POST or None)
    if form.is_valid():
        print(form.data['klasa'])
        obj = Uczniowie.objects.filter(klasa=form.data['klasa'])    
    context={
        "uczniowie" : obj,
        'form' : form
    }
    return render(request, 'obecnosc/obecnosc.html', context)