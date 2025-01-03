from rest_framework import serializers
from reservation.models import Reservation

class ReservationUpdateSerializer(serializers.ModelSerializer):

    client = serializers.IntegerField(required=True)
    car = serializers.IntegerField(required=True)
    status = serializers.CharField(max_length=50, required=False)
    processedby = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Reservation
        fields = ['client', 'car', 'status', 'processedby']  

    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.car = validated_data.get('car', instance.car)
        instance.status = validated_data.get('status', instance.status)
        instance.processedby = validated_data.get('processedby', instance.processedby)

        instance.save()
        return instance