from django.db import models

# Create your models here.
class Atracoes(models.Model):
    name = models.CharField( max_length= 100)
    description = models.TextField()
    business = models.TextField()
    minimum_age = models.IntegerField()


    def __str__(self):
        return self.name



