from django.contrib import admin
from obecnosc.models import Uczniowie

class UczniowieAdmin(admin.ModelAdmin):
    list_display = ('id_ucznia', 'numer_w_dzienniku', 'nazwisko_imie', 'klasa')
    search_fields = ('id_ucznia', 'numer_w_dzienniku', 'nazwisko_imie', 'klasa')
    readonly_fields = ()
    # asdas
    # asdsadas
<<<<<<< HEAD
    #Test pobrania
=======
    #safasfasf
>>>>>>> 3757f716cefcc4980e468ca807a30a779035130d

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Uczniowie, UczniowieAdmin)