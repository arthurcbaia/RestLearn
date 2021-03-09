from rest_framework.viewsets import ModelViewSet
from location.models import Location
from location.api.serializers import LocationSerializer

class LocationViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer