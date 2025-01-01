from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name

