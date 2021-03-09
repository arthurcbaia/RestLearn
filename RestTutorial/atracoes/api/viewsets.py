from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracoes
from atracoes.api.serializers import AtracoesSerializer
from rest_framework.filters import SearchFilter

class AtracoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer
    filter_fields = ('name','minimum_age')
    filter_backends = [SearchFilter]
    search_fields = ('name','minimum_age')