from django.db import models

from app_localtion_car_ssr_project.shared.models.modelWrapper import ModelWrapper

class Car(ModelWrapper):
    car_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    rentalprice = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        db_table = "car"