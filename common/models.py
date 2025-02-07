from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class UBlob(models.Model):
    blob_id = models.AutoField(primary_key=True)
    blob = models.BinaryField(null=False, blank=False)  # Use BinaryField for binary data
    nature = models.CharField(max_length=50, null=False, blank=False)

    # Generic Foreign Key fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    user = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = "ublob"
        verbose_name = "UBlob"
        verbose_name_plural = "Ublobs"
        

    def __str__(self):
        return f"Blob {self.blob_id} for {self.user.username}"