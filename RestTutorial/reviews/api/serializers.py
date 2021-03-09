
from rest_framework.serializers import ModelSerializer 
from reviews.models import Review

class ReviewsSerializer(ModelSerializer):
     class Meta:
        model = Review
        fields = ['id','user','review','approved','date']