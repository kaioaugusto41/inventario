from rest_framework import viewsets, permissions
from app.models import Impressoras
from api.serializers.impressorasS import ImpressorasSerializer

class ImpressorasViewSet(viewsets.ModelViewSet):
    queryset = Impressoras.objects.all()
    serializer_class = ImpressorasSerializer
    permission_classes = [permissions.IsAuthenticated]