
from rest_framework.serializers import ModelSerializer 
from Turismo.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
class PontoTuristicoSerializer(ModelSerializer):
   attractions = AtracoesSerializer(many = True)
   class Meta:
      model = PontoTuristico
      fields = ['id', 'name', 'description','recommended','attractions','comments','review','location']