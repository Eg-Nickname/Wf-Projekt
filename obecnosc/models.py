from pyexpat import model
from django.db import models


class Uczniowie(models.Model):
    KLASY = (
        ('1a_gr1', 'Klasa 1a grupa 1'),
        ('1a_gr2', 'Klasa 1a grupa 2'),
        ('1b_gr1', 'Klasa 1b grupa 1'),
        ('1b_gr2', 'Klasa 1b grupa 2'),
        ('1c_gr1', 'Klasa 1c grupa 1'),
        ('1c_gr2', 'Klasa 1c grupa 2'),
        ('1t_gr1', 'Klasa 1t grupa 1'),
        ('1t_gr2', 'Klasa 1t grupa 2'),
        ('2a_gr1', 'Klasa 2a grupa 1'),
        ('2a_gr2', 'Klasa 2a grupa 2'),
        ('2b_gr1', 'Klasa 2b grupa 1'),
        ('2b_gr2', 'Klasa 2b grupa 2'),
        ('2c_gr1', 'Klasa 2c grupa 1'),
        ('2c_gr2', 'Klasa 2c grupa 2'),
        ('2t_gr1', 'Klasa 2t grupa 1'),
        ('2t_gr2', 'Klasa 2t grupa 2'),
        ('3a_gr1', 'Klasa 3a grupa 1'),
        ('3a_gr2', 'Klasa 3a grupa 2'),
        ('3b_gr1', 'Klasa 3b grupa 1'),
        ('3b_gr2', 'Klasa 3b grupa 2'),
        ('3c_gr1', 'Klasa 3c grupa 1'),
        ('3c_gr2', 'Klasa 3c grupa 2'),
        ('3t_gr1', 'Klasa 3t grupa 1'),
        ('3t_gr2', 'Klasa 3t grupa 2'),
        ('4a_gr1', 'Klasa 4a grupa 1'),
        ('4a_gr2', 'Klasa 4a grupa 2'),
        ('4b_gr1', 'Klasa 4b grupa 1'),
        ('4b_gr2', 'Klasa 4b grupa 2'),
        ('4c_gr1', 'Klasa 4c grupa 1'),
        ('4c_gr2', 'Klasa 4c grupa 2'),
        ('4t_gr1', 'Klasa 4t grupa 1'),
        ('4t_gr2', 'Klasa 4t grupa 2'),
        ('5t_gr1', 'Klasa 5t grupa 1'),
        ('5t_gr2', 'Klasa 5t grupa 2'),
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