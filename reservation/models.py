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

    reservation_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clients', null=False, blank=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reservations', null=False, blank=False)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING, null=False, blank=False)
    processedby = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='agents', null=True, blank=True)
    def __str__(self):
        return self.client,self.car
    
    class Meta:
        db_table = "reservation"
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

