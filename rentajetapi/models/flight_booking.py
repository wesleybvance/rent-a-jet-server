from django.db import models
from .flight import Flight
from .customer import Customer

class FlightBooking(models.Model):

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField()
    payment_method = models.CharField(max_length=50)
