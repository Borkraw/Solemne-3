from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Plan_movil
# Clase serializadora de Usuarios
class PlanesmovilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan_movil 
        fields = ['id','title','precio','description','publishedBy','views']

# Clase de viewset que hace el puente entre bd - serealizacion
class PlanesmovilViewSet(viewsets.ModelViewSet):
    # Query que ejecutara a la bd
    queryset = Plan_movil.objects.all()
    serializer_class = PlanesmovilSerializer

router = routers.DefaultRouter()
router.register(r'', PlanesmovilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]