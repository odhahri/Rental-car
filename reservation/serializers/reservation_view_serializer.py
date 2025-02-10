from rest_framework import serializers
from agent.models import Agent
from cars.models import Car
from reservation.models import Reservation
from client.models import Client  

class ReservationSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='reservation_id')
    reservation_client_key = serializers.SerializerMethodField() 
    reservation_car_key = serializers.SerializerMethodField()
    reservation_start_date = serializers.DateTimeField(source='start_date')
    reservation_end_date = serializers.DateTimeField(source='end_date')
    reservation_status = serializers.CharField(source='status')
    reservation_processed_by = serializers.SerializerMethodField()
    reservation_created_at = serializers.DateTimeField(source='created_at')
    reservation_updated_at = serializers.DateTimeField(source='updated_at')

    def get_reservation_client_key(self, obj):

        client_id = obj.client_id  
        try:
            client = Client.objects.get(client_id=client_id)  
            return client.username  
        except Client.DoesNotExist:
            return None 
        
    def get_reservation_processed_by(self, obj):

        agent_id = obj.processedby_id 
        try:
            agent = Agent.objects.get(agent_id=agent_id)  
            return agent.username  
        except Agent.DoesNotExist:
            return None  
        
    def get_reservation_car_key(self, obj):

        car_id = obj.car_id  
        try:
            car = Car.objects.get(car_id=car_id)  
            return car.name  
        except Car.DoesNotExist:
            return None 
        