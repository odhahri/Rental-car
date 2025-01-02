
from app_localtion_car_ssr_project.shared.models.modelWrapper import ModelWrapper
from django.db import models

class BaseUser(ModelWrapper):
    username = models.CharField(max_length=50, unique=True, default='')
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50 , default='')
    email = models.EmailField(max_length=50, unique=True,default='')
    phone = models.CharField(max_length=50  , default='')
    #  base 64 image 
    image = models.TextField(max_length=500, blank=True, null=True)
    class Meta:
        abstract = True

