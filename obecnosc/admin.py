from django.contrib import admin
from obecnosc.models import Uczniowie

class UczniowieAdmin(admin.ModelAdmin):
    list_display = ('id_ucznia', 'numer_w_dzienniku', 'nazwisko_imie', 'klasa')
    search_fields = ('id_ucznia', 'numer_w_dzienniku', 'nazwisko_imie', 'klasa')
    readonly_fields = ()
    # asdas
    # asdsadas
    #Test pobrania

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Uczniowie, UczniowieAdmin)