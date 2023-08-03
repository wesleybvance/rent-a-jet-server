from django.db import models
from .airport import Airport

class Flight(models.Model):

    name = models.CharField(max_length=100)
    departure_airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
    destination_airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_airport')
    price = models.BigIntegerField()
