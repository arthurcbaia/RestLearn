from django.db import models

# Create your models here.
class Location(models.Model):
    adress = models.CharField( max_length = 100)
    city = models.CharField( max_length = 100)
    state = models.CharField( max_length = 100)
    country = models.CharField( max_length = 100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank= True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank= True)


    def __str__(self):
        return self.adress
