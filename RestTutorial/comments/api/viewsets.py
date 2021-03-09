from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from comments.api.serializers import CommentsSerializer

class CommentsViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer