from django.db import models

from common.shared.models.modelWrapper import ModelWrapper


class Car(ModelWrapper):
    car_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    brand = models.CharField(max_length=200, null=False, blank=False)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField(null=False, blank=False)
    rentalprice = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        db_table = "car"