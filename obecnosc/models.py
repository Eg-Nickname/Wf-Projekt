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
    imie              = models.CharField(verbose_name="Imie", max_length=64, unique=False)    
    nazwisko          = models.CharField(verbose_name="Nazwisko", max_length=64, unique=False)
    klasa             = models.CharField(verbose_name="Klasa", max_length=64, unique=False, choices=KLASY)

    def __str__(self):
        return str(self.id_ucznia)