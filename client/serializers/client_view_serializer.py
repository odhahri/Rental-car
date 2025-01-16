from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='client_id')
    user_name = serializers.CharField(source='username')
    user_email = serializers.EmailField(source='email')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    client_phone_number = serializers.CharField(source='phone')
    client_image = serializers.CharField(source='image')
    client_identity = serializers.CharField(source='identity')
    client_created_at = serializers.DateTimeField(source='created_at')
    client_updated_at = serializers.DateTimeField(source='updated_at')
