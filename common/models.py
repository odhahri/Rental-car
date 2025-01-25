from django.db import models
from django.contrib.contenttypes.models import ContentType


class UBlob(models.Model):
    blob_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='blobs', null=False, blank=False)
    blob = models.TextField(unique=True, null=False, blank=False)
    nature = models.CharField(max_length=50, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)
    class Meta:
        db_table = "ublob"
        verbose_name = "UBlob"
        verbose_name_plural = "Ublobs"
