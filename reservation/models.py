from django.db import models

from agent.models import Agent
from app_localtion_car_ssr_project.shared.models.modelWrapper import ModelWrapper
from cars.models import Car
from client.models import Client

class Reservation(ModelWrapper):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    reservation_id = models.AutoField(primary_key=True, default=0)
    date = models.DateField(auto_now=False, auto_now_add=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clients')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reservations')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    processedby = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agents', null=True, blank=True)
    def __str__(self):
        return self.client,self.car,self.date
    
    class Meta:
        db_table = "reservation"
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

