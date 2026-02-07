from django.db import models
from django.contrib.auth.models import User

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    rozmiar = models.CharField(max_length=20)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"
    
    def __str__(self):
        return self.nazwa

class Dostawa(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    dostawca = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    ilosc = models.IntegerField()
    
    class Meta:
        verbose_name = "Dostawa"
        verbose_name_plural = "Dostawy"
    
    def __str__(self):
        return f"{self.dostawca} - {self.material}"

class Produkcja(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    ilosc = models.IntegerField()
    partia = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Produkcja"
        verbose_name_plural = "Produkcja"
    
    def __str__(self):
        return f"{self.produkt.nazwa} - {self.partia}"

class Magazyn(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.IntegerField(default=0)
    ostatnia_aktualizacja = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Magazyn"
        verbose_name_plural = "Magazyny"
    
    def __str__(self):
        return f"{self.produkt.nazwa} - {self.ilosc} szt"

class Zamowienie(models.Model):
    klient = models.CharField(max_length=100)
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    data_zamowienia = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='oczekuje')
    
    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"
    
    def __str__(self):
        return f"{self.klient} - {self.produkt.nazwa}"
