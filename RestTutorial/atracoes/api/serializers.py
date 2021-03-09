from rest_framework.serializers import ModelSerializer 
from atracoes.models import Atracoes

class AtracoesSerializer(ModelSerializer):
     class Meta:
        model = Atracoes
        fields = ['id', 'name', 'description', 'business', 'minimum_age']