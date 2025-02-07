from django.db import models

from common.shared.models.baseUser import BaseUser


class Client(BaseUser):
    client_id = models.AutoField(primary_key=True)
    # blob base 64 image
    identity = models.CharField(max_length=500, blank=False, null=False, default='')


    def __str__(self):
        return self.client_id
    class Meta:
        db_table = "client"
        verbose_name = "Client"
        verbose_name_plural = "Clients"



