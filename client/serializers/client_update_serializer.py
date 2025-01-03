from rest_framework import serializers
from client.models import Client

class ClientUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['username', 'fname', 'lname', 'email', 'phone','identity']
        extra_kwargs = {
            'username': {'required': False},
            'fname': {'required': False},
            'lname': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'identity': {'required': False},
        }
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.identity = validated_data.get('identity', instance.identity)
                
        instance.save()
        return instance