from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Contactos
# Clase serializadora de Usuarios
class ContactosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contactos
        fields = ['nombre','numero','email','tipo','motivo','estado']

# Clase de viewset que hace el puente entre bd - serealizacion
class ContactosViewSet(viewsets.ModelViewSet):
    # Query que ejecutara a la bd
    queryset = Contactos.objects.all()
    serializer_class = ContactosSerializer

router = routers.DefaultRouter()
router.register(r'', ContactosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]