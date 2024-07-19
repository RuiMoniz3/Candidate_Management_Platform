from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, RecrutadorViewSet, VagaViewSet, CandidatoViewSet, CandidaturaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'recrutadores', RecrutadorViewSet)
router.register(r'vagas', VagaViewSet)
router.register(r'candidatos', CandidatoViewSet)
router.register(r'candidaturas', CandidaturaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
]


