from rest_framework import serializers
from client.models import Client

class ClientCreateInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['username', 'fname', 'lname', 'email', 'phone','identity']
        extra_kwargs = {
            'username': {'required': True},
            'fname': {'required': True},
            'lname': {'required': True},
            'email': {'required': True},
            'phone': {'required': True},
            'identity': {'required': True},
        }

    def create(self, validated_data: dict):
        return Client.objects.create(
            username=validated_data.get('username'),
            fname=validated_data.get('fname'),
            lname=validated_data.get('lname'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
        )

class ClientCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'