from rest_framework import serializers
from agent.models import Agent

class AgentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ['username', 'fname', 'lname', 'email', 'phone']
        extra_kwargs = {
            'username': {'required': False},
            'fname': {'required': False},
            'lname': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
        }
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
                
        instance.save()
        return instance