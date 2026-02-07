from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'produkty', ProduktViewSet)
router.register(r'dostawy', DostawaViewSet)
router.register(r'produkcja', ProdukcjaViewSet)
router.register(r'magazyn', MagazynViewSet)
router.register(r'zamowienia', ZamowienieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
