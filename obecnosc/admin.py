from django.contrib import admin
from obecnosc.models import Uczniowie, Obecnosci

class UczniowieAdmin(admin.ModelAdmin):
    list_display = ('id_ucznia', 'numer_w_dzienniku', 'nazwisko_imie', 'klasa')
    search_fields = ('id_ucznia', 'numer_w_dzienniku', 'nazwisko_imie', 'klasa')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ObecnosciAdmin(admin.ModelAdmin):
    list_display = ('id_obecnosci', 'uczen', 'status', 'data')
    search_fields = ('id_obecnosci', 'uczen', 'status', 'data')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Uczniowie, UczniowieAdmin)
admin.site.register(Obecnosci, ObecnosciAdmin)