from rest_framework import serializers
from .models import Produkt, Dostawa, Produkcja, Magazyn, Zamowienie

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = '__all__'

class DostawaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dostawa
        fields = '__all__'

class ProdukcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkcja
        fields = '__all__'

class MagazynSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazyn
        fields = '__all__'

class ZamowienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = '__all__'
