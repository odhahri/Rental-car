from rest_framework import serializers

from django.contrib.contenttypes.models import ContentType

from common.models import UBlob


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='client_id')
    user_name = serializers.CharField(source='username')
    user_email = serializers.EmailField(source='email')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    user_phone_number = serializers.IntegerField(source='phone')
    user_identity = serializers.CharField(source='identity')
    user_created_at = serializers.DateTimeField(source='created_at')
    user_updated_at = serializers.DateTimeField(source='updated_at')

    # Add blobs as a nested list
    user_blobs = serializers.SerializerMethodField()

    def get_user_blobs(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        blobs = UBlob.objects.filter(user=content_type, user_id=obj.client_id)  # Filter blobs for this client
        return [
            {
                "blob_id": blob.blob_id,
                "blob": blob.blob,
                "nature": blob.nature,
                "order": blob.order
            }
            for blob in blobs
        ]
