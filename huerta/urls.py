from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgricultorViewSet, CultivoViewSet

router = DefaultRouter()
router.register(r'agricultores', AgricultorViewSet)
router.register(r'cultivos', CultivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]