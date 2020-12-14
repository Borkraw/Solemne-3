from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Plan_hogar
# Clase serializadora de Usuarios
class PlaneshogarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan_hogar 
        fields = ['id','title','precio','description','publishedBy','views']

# Clase de viewset que hace el puente entre bd - serealizacion
class PlaneshogarViewSet(viewsets.ModelViewSet):
    # Query que ejecutara a la bd
    queryset = Plan_hogar.objects.all()
    serializer_class = PlaneshogarSerializer

router = routers.DefaultRouter()
router.register(r'', PlaneshogarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]