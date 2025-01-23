from django.db import models

from app_localtion_car_ssr_project.shared.models.baseUser import BaseUser

class Client(BaseUser):
    client_id = models.AutoField(primary_key=True)
    # blob base 64 image
    identity = models.CharField(max_length=500, blank=False, null=False, default='')


    def __str__(self):
        return self.date
    class Meta:
        db_table = "client"
        verbose_name = "Client"
        verbose_name_plural = "Clients"

class CBlob(models.Model):
    blob_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='blobs', null=False, blank=False)
    blob = models.TextField(unique=True, null=False, blank=False)

    class Meta:
        db_table = "cblob"
        verbose_name = "CBlob"
        verbose_name_plural = "CBlobs"


