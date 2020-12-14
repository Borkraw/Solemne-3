from django.contrib import admin
from django.urls import path, include
from rest_framework import routers,serializers, viewsets
from django.contrib.auth.models import User

# Clase serializadora de Usuarios
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ['url','username','email','is_staff']

# Clase de viewset que hace el puente entre bd - serealizacion
class UserViewSet(viewsets.ModelViewSet):
    # Query que ejecutara a la bd
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('planesmovil/', include('planesmovil.urls')),
    path('planeshogar/', include('planeshogar.urls')),
    path('contactos/', include('contacto.urls')),
    path('admin/', admin.site.urls),
]