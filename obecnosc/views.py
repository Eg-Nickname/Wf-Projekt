from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm

from .models import Uczniowie, Obecnosci

def obecnosc_view(request):
    context={}
    obj = Uczniowie.objects.filter()
    context={
        "uczniowie" : obj
    }
    return render(request, 'obecnosc/obecnosc.html', context)