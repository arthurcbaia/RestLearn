from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from Turismo.models import PontoTuristico
from Turismo.api.serializers import PontoTuristicoSerializer
from rest_framework.decorators import action


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
   
    serializer_class = PontoTuristicoSerializer
    lookup_field = 'name'
    def get_queryset(self): # Permite mudar o retorno da queryset, no caso influenciando os metodos
        return PontoTuristico.objects.filter(
            recommended = True)
    # def list(self, request, *args, **kwargs): #Permite reescrever o metodo list 
    #     return Response({'teste':123})
    #def create(self, request, *args, **kwargs): 
    #def destroy(self, request, *args, **kwargs):
        #pass

    @action(methods = ['get'], detail = True) # Detail == true, relacionado a ser uma action não relacionada a end point, no caso Pontoturistico
    def denunciar(self, request, pk = None): #Action criada pelo proprio usuario, o fato de ser detail = True, faz com que essa action sirva para um id espefico, ai o porque de receber pk no metodo
        pass
