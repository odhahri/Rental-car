from rest_framework import serializers
from agent.models import Agent

class AgentCreateInputSerializer(serializers.ModelSerializer):
    # image = serializers.CharField(max_length=50, required=True, allow_blank=True)

    class Meta:
        model = Agent
        fields = ['username', 'fname', 'lname', 'email', 'phone', 'image']
        extra_kwargs = {
            'username': {'required': True},
            'fname': {'required': True},
            'lname': {'required': True},
            'email': {'required': True},
            'phone': {'required': True},
        }

    def create(self, validated_data: dict):
        return Agent.objects.create(
            username=validated_data.get('username'),
            fname=validated_data.get('fname'),
            lname=validated_data.get('lname'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            image=validated_data.get('image')

        )

class AgentCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'