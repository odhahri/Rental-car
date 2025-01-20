from rest_framework import serializers

class AgentSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='agent_id')
    user_name = serializers.CharField(source='username')
    user_email = serializers.EmailField(source='email')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    user_phone_number = serializers.CharField(source='phone')
    user_image = serializers.ImageField(source='image')
    user_created_at = serializers.DateTimeField(source='created_at')
    user_updated_at = serializers.DateTimeField(source='updated_at')
