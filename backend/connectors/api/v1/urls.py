from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import spr65newcinaViewSet

router = DefaultRouter()
router.register("spr65newcina", spr65newcinaViewSet, basename="spr65newcina")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
