from rest_framework import serializers
from cars.models import Car
from client.models import Client
from reservation.models import Reservation

class ReservationCreateInputSerializer(serializers.Serializer):
    reservation_client_key = serializers.IntegerField(required=True)
    reservation_car_key = serializers.IntegerField(required=True)
    reservation_processed_by = serializers.CharField(max_length=50, required=False)

    def create(self, validated_data):
        # Get the client and car instances
        client_instance = Client.objects.get(id=validated_data.get('reservation_client_key'))
        car_instance = Car.objects.get(id=validated_data.get('reservation_car_key'))
        
        # Create and return the Reservation instance
        return Reservation.objects.create(
            client=client_instance,
            car=car_instance,
            processedby=validated_data.get('reservation_processed_by')
        )


class ReservationCreateOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id')
    reservation_client_key = serializers.IntegerField(source='client')
    reservation_car_key = serializers.IntegerField(source='car')
    reservation_status = serializers.CharField(source='status')
    reservation_processed_by = serializers.CharField(source='processedby')
    reservation_created_at = serializers.DateTimeField(source='created_at')
    reservation_updated_at = serializers.DateTimeField(source='updated_at')
