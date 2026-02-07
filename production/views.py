from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import *
from .serializers import *

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class ProduktViewSet(viewsets.ModelViewSet):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer

    @action(detail=False, methods=['get'])
    def niski_stan(self, request):
        niskie = Magazyn.objects.filter(ilosc__lt=10).select_related('produkt')
        dane = [{'produkt': m.produkt.nazwa, 'ilosc': m.ilosc} for m in niskie]
        return Response(dane)

class DostawaViewSet(viewsets.ModelViewSet):
    queryset = Dostawa.objects.all()
    serializer_class = DostawaSerializer
    permission_classes = [IsAdminUser]

class ProdukcjaViewSet(viewsets.ModelViewSet):
    queryset = Produkcja.objects.all()
    serializer_class = ProdukcjaSerializer

    @action(detail=False, methods=['get'])
    def miesieczne_podsumowanie(self, request):
        from datetime import timedelta
        from django.utils import timezone
        
        miesiac_temu = timezone.now() - timedelta(days=30)
        produkcja = Produkcja.objects.filter(data__gte=miesiac_temu)
        
        podsumowanie = produkcja.values('produkt__nazwa').annotate(
            calkowita_ilosc=Sum('ilosc')
        ).order_by('-calkowita_ilosc')
        
        return Response(list(podsumowanie))

class MagazynViewSet(viewsets.ModelViewSet):
    queryset = Magazyn.objects.all()
    serializer_class = MagazynSerializer

    @action(detail=False, methods=['get'])
    def stan_magazynowy(self, request):
        stan = Magazyn.objects.select_related('produkt').all()
        dane = [{'produkt': s.produkt.nazwa, 'ilosc': s.ilosc, 'ostatnia_aktualizacja': s.ostatnia_aktualizacja} for s in stan]
        return Response(dane)

class ZamowienieViewSet(viewsets.ModelViewSet):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer

    @action(detail=False, methods=['get'])
    def aktywne_zamowienia(self, request):
        aktywne = Zamowienie.objects.filter(status='oczekuje').select_related('produkt')
        dane = [{'klient': z.klient, 'produkt': z.produkt.nazwa, 'ilosc': z.ilosc, 'data': z.data_zamowienia} for z in aktywne]
        return Response(dane)
