from rest_framework import serializers

from client.models import Client
from client.serializers.client_create_serializer import ClientCreateBlobSerializer


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='client_id')
    user_name = serializers.CharField(source='username')
    user_email = serializers.EmailField(source='email')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    user_phone_number = serializers.IntegerField(source='phone')
    # user_image = serializers.ImageField(source='image')
    user_identity = serializers.CharField(source='identity')
    user_created_at = serializers.DateTimeField(source='created_at')
    user_updated_at = serializers.DateTimeField(source='updated_at')
    user_image = ClientCreateBlobSerializer(source='blobs', many=True)

