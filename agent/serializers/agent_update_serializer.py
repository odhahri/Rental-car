from rest_framework import serializers
from agent.models import Agent

class AgentUpdateSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=150, required=False)
    user_first_name = serializers.CharField(max_length=50, required=False)
    user_last_name = serializers.CharField(max_length=50, required=False)
    user_email = serializers.EmailField(required=False)
    user_phone_number = serializers.CharField(max_length=20, required=False)
    user_image = serializers.CharField(max_length=500, required=False, allow_blank=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('user_name', instance.username)
        instance.fname = validated_data.get('user_first_name', instance.fname)
        instance.lname = validated_data.get('user_last_name', instance.lname)
        instance.email = validated_data.get('user_email', instance.email)
        instance.phone = validated_data.get('user_phone_number', instance.phone)
        instance.image = validated_data.get('user_image', instance.image)
        
        instance.save()
        return instance
