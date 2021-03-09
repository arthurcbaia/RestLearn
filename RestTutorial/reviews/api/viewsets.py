from rest_framework.viewsets import ModelViewSet
from reviews.models import Review
from reviews.api.serializers import ReviewsSerializer

class ReviewsViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer