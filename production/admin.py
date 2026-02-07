from django.contrib import admin
from .models import Produkt, Dostawa, Produkcja, Magazyn, Zamowienie

admin.site.register(Produkt)
admin.site.register(Dostawa)
admin.site.register(Produkcja)
admin.site.register(Magazyn)
admin.site.register(Zamowienie)