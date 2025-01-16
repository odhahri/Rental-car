from rest_framework import serializers
from reservation.models import Reservation

class ReservationUpdateSerializer(serializers.Serializer):
    reservation_client_key = serializers.IntegerField(required=True)
    reservation_car_key = serializers.IntegerField(required=True)
    reservation_status = serializers.CharField(max_length=50, required=False)
    processed_by = serializers.CharField(max_length=50, required=False)

    def update(self, instance, validated_data):
        instance.client = validated_data.get('reservation_client_key', instance.client)
        instance.car = validated_data.get('reservation_car_key', instance.car)
        instance.status = validated_data.get('reservation_status', instance.status)
        instance.processedby = validated_data.get('processed_by', instance.processedby)

        instance.save()
        return instance
