from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.http import request

from django.utils.translation import gettext as _

from .models import Uczniowie, Obecnosci

class ObecnoscForm(forms.ModelForm):
    class Meta:
        model = Uczniowie
        fields={
            'klasa'
        }
