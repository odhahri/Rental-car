from rest_framework import serializers
from client.models import  Client

class ClientCreateInputSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=150)
    user_first_name = serializers.CharField(max_length=50)
    user_last_name = serializers.CharField(max_length=50)
    user_email = serializers.EmailField()
    user_phone_number = serializers.CharField(max_length=20)
    user_identity = serializers.CharField(max_length=500)
    
    def create(self, validated_data):
        return Client.objects.create(
            username=validated_data.get('user_name'),
            fname=validated_data.get('user_first_name'),
            lname=validated_data.get('user_last_name'),
            email=validated_data.get('user_email'),
            phone=validated_data.get('user_phone_number'),
            identity=validated_data.get('user_identity')
        )
    
class ClientCreateOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='client_id')
    user_name = serializers.CharField(source='username')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    user_email = serializers.EmailField(source='email')
    user_phone_number = serializers.CharField(source='phone')
    user_identity = serializers.CharField(source='identity')
    user_created_at = serializers.DateTimeField(source='created_at')
    user_updated_at = serializers.DateTimeField(source='updated_at')