from rest_framework import serializers
from agent.models import Agent
from cars.models import Car
from client.models import Client
from reservation.models import Reservation

class ReservationUpdateSerializer(serializers.Serializer):
    reservation_client_key = serializers.IntegerField(required=True)
    reservation_car_key = serializers.IntegerField(required=True)
    # status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING, null=False, blank=False)
    reservation_status = serializers.CharField(max_length=10, required=False)
    reservation_processed_by = serializers.IntegerField(required=True)
    reservation_start_date = serializers.DateTimeField(required=True)
    reservation_end_date = serializers.DateTimeField(required=True)

    def update(self, instance, validated_data):
        instance.client = Client.objects.get(client_id = validated_data.get('reservation_client_key'))
        instance.car = Car.objects.get(car_id = validated_data.get('reservation_car_key'))
        instance.status = validated_data.get('reservation_status', instance.status)
        instance.processedby = Agent.objects.get(agent_id = validated_data.get('reservation_processed_by'))
        instance.start_date = validated_data.get('reservation_start_date', instance.start_date)
        instance.end_date = validated_data.get('reservation_end_date', instance.end_date)

        instance.save()
        return instance
