from django.db import models

class Airport(models.Model):
    city = models.CharField(max_length=55)
    code = models.CharField(max_length=3)
