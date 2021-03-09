from django.db import models
from atracoes.models import Atracoes
from comments.models import Comments
from reviews.models import Review 
from location.models import Location
# Create your models here.
class PontoTuristico(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    recommended = models.BooleanField( default = False)
    attractions = models.ManyToManyField(Atracoes)
    comments = models.ManyToManyField(Comments)
    review = models.ManyToManyField(Review)
    location = models.ForeignKey(Location, on_delete = models.CASCADE , null = True, blank = True)
    
    
    def __str__(self):
        return self.name


