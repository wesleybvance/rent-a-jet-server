from django.db import models
from .airport import Airport

class Flight(models.Model):

    name = models.CharField(max_length=100)
    departure_airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE)
    destination_airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE)
    price = models.BigIntegerField()
