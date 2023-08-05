from django.db import models
from .airport import Airport

class Customer(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    phone_number = models.IntegerField()
    profile_image = models.CharField(max_length=200)
    home_airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    uid = models.CharField(max_length=200, default='')
