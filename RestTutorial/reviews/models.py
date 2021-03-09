from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review = models.DecimalField(default = 0, max_digits = 2, decimal_places = 1)
    approved = models.BooleanField( default = True)
    date = models.DateField(auto_now_add= True )
    

    def __str__(self):
        return self.user.username
