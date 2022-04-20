from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm
from urllib3 import HTTPResponse

def obecnosc_view(request):
    return render(request, 'obecnosc/obecnosc.html', {})