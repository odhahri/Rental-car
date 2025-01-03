from rest_framework import serializers
from agent.models import Agent

class AgentCreateInputSerializer(serializers.ModelSerializer):
    # image = serializers.CharField(max_length=50, required=True, allow_blank=True)

    class Meta:
        model = Agent
        fields = ['username', 'fname', 'lname', 'email', 'phone']
        extra_kwargs = {
            'username': {'required': True},
            'fname': {'required': True},
            'lname': {'required': True},
            'email': {'required': True},
            'phone': {'required': True},
        }

    def create(self, validated_data: dict):
        return Agent.objects.create(
            name=validated_data.get('name'),
            color=validated_data.get('color'),
            year=validated_data.get('year'),
            price=validated_data.get('price'),
            image=validated_data.get('image')
        )

class AgentCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'