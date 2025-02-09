from rest_framework import serializers
from agent.models import Agent
from cars.models import Car
from client.models import Client
from reservation.models import Reservation

class ReservationCreateInputSerializer(serializers.Serializer):
    reservation_client_key = serializers.IntegerField(required=True)
    reservation_car_key = serializers.IntegerField(required=True)
    reservation_processed_by = serializers.CharField(max_length=50, required=False)
    reservation_start_date = serializers.DateTimeField(required=True)
    reservation_end_date = serializers.DateTimeField(required=True)
    def create(self, validated_data):
        # Get the client and car instances
        client_instance = Client.objects.get(client_id=validated_data.get('reservation_client_key'))
        car_instance = Car.objects.get(car_id=validated_data.get('reservation_car_key'))
        processedby = Agent.objects.get(agent_id=validated_data.get('reservation_processed_by'))
        
        # Create and return the Reservation instance
        return Reservation.objects.create(
            client=client_instance,
            car=car_instance,
            processedby=processedby,
            start_date=validated_data.get('reservation_start_date'),
            end_date=validated_data.get('reservation_end_date')
        )


class ReservationCreateOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='reservation_id')
    reservation_client_key = serializers.IntegerField(source='client_id')
    reservation_car_key = serializers.IntegerField(source='car_id')
    reservation_status = serializers.CharField(source='status')
    reservation_processed_by = serializers.CharField(source='processedby')
    reservation_created_at = serializers.DateTimeField(source='created_at')
    reservation_updated_at = serializers.DateTimeField(source='updated_at')
    reservation_start_date = serializers.DateTimeField(source='start_date')
    reservation_end_date = serializers.DateTimeField(source='end_date')
