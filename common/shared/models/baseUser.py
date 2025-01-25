
from django.db import models

from common.shared.models.modelWrapper import ModelWrapper

class BaseUser(ModelWrapper):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    fname = models.CharField(max_length=50, null=False, blank=False)
    lname = models.CharField(max_length=50 , null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=50  , unique=True, null=False, blank=False)

    class Meta:
        abstract = True

