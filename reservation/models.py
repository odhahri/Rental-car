from django.db import models

from cars.models import Car
from client.models import Client

class Reservation(models.Model):
    date = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clients')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reservations')
    # status = models.enums('pending', 'approved', 'rejected')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client,self.car,self.date

