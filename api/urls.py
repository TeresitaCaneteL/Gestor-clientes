from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, CotizacionViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'cotizaciones', CotizacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
