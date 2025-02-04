from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from client.models import Client
from common.models import UBlob  # Import your models

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
    user_blobs = serializers.SerializerMethodField()  # Custom field for UBlob instances

    def get_user_blobs(self, obj):
        # Get the ContentType for the Client model
        content_type = ContentType.objects.get_for_model(Client)

        # Filter UBlob instances for this Client
        ublobs = UBlob.objects.filter(content_type=content_type, object_id=obj.client_id)

        # Serialize the UBlob instances
        return [
            {
                'blob_id': ublob.blob_id,
                'blob': ublob.blob,
                'nature': ublob.nature,
                'order': ublob.order
            }
            for ublob in ublobs
        ]