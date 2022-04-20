from pyexpat import model
from django.db import models


class Uczniowie(models.Model):
    KLASY = (
        ('1a_gr1', 'Klasa 1a grupa 1'),
        ('1a_gr2', 'Klasa 1a grupa 2'),
        ('1b_gr1', 'Klasa 1b grupa 1'),
        ('1b_gr2', 'Klasa 1b grupa 2'),
    )

    id_ucznia         = models.BigAutoField(verbose_name="Id ucznia", primary_key=True)
    numer_w_dzienniku = models.PositiveIntegerField(verbose_name="Numer w dzienniku", default=0)
    nazwisko_imie     = models.CharField(verbose_name="Imie i nazwisko", max_length=128, default="", unique=False)    
    klasa             = models.CharField(verbose_name="Klasa", max_length=64, unique=False, choices=KLASY)

    def __str__(self):
        return str(self.nazwisko_imie)

class Obecnosci(models.Model):
    Statusy = (
        ('OB', 'Obecny'),
        ('ZW', 'Zwolniony'),
        ('BS', 'Brak Stroju'),
        ('NB', 'Nieobecny'),
    )

    id_obecnosci = models.BigAutoField(verbose_name="Id obecnosci", primary_key=True)
    uczen = models.ForeignKey(Uczniowie, null=True, on_delete=models.SET_NULL, related_name='Uczen', verbose_name="Uczeń")
    status = models.CharField(verbose_name="Status", max_length=64, unique=False, choices=Statusy)
    data = models.DateField(verbose_name='Data sprawdzania', auto_now_add=True)