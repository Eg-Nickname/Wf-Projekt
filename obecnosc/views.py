from multiprocessing import context
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm

from .models import Uczniowie, Obecnosci

from .forms import ObecnoscForm

def obecnosc_view(request):
    context={}
    for id in request.POST:
        if id != "csrfmiddlewaretoken" and id != "klasa":
            uczen = Uczniowie.objects.get(id_ucznia=id)
            status = request.POST.get(id)
            Obecnosc = Obecnosci(uczen = uczen , status = status)
            Obecnosc.save()
    form = ObecnoscForm(request.POST or None)
    if form.is_valid():
        obj = Uczniowie.objects.filter(klasa=form.data['klasa'])
    else:
        obj = Uczniowie.objects.none()    
    context={
        'uczniowie' : obj,
        'form' : form
    }
    return render(request, 'obecnosc/obecnosc.html', context)
def dziennik_view(request):
    context = {}
    form = ObecnoscForm(request.POST or None)
    if form.is_valid():
        obj2 = Uczniowie.objects.filter(klasa=form.data['klasa'])
        obj = Obecnosci.objects.filter(uczen__klasa=form.data['klasa'])
    else:
        obj2 = Uczniowie.objects.none()
        obj = Obecnosci.objects.none()
    context={
        'obecnosci' : obj,
        'uczniowie' : obj2,
        'form' : form
    }
    return render(request, 'obecnosc/dziennik.html', context)