from rest_framework import serializers
from agent.models import Agent

class AgentCreateInputSerializer(serializers.Serializer):
    # Input Fields
    user_name = serializers.CharField(max_length=150, required=True)
    user_first_name = serializers.CharField(max_length=50, required=True)
    user_last_name = serializers.CharField(max_length=50, required=True)
    user_email = serializers.EmailField(max_length=100,required=True)
    user_phone_number = serializers.CharField(max_length=20, required=True)
    user_image = serializers.CharField(max_length=500, required=False, allow_blank=True)

    def create(self, validated_data):
        return Agent.objects.create(
            username=validated_data.get('user_name'),
            fname=validated_data.get('user_first_name'),
            lname=validated_data.get('user_last_name'),
            email=validated_data.get('user_email'),
            phone=validated_data.get('user_phone_number'),
            image=validated_data.get('user_image')
        )


class AgentCreateOutputSerializer(serializers.Serializer):
    # Output Fields
    id = serializers.IntegerField(source='agent_id')
    user_name = serializers.CharField(source='username')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    user_email = serializers.EmailField(source='email')
    user_phone_number = serializers.CharField(source='phone')
    user_image = serializers.CharField(source='image')
    user_created_at = serializers.DateTimeField(source='created_at')
    user_updated_at = serializers.DateTimeField(source='updated_at')
