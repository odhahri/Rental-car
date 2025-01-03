from rest_framework import serializers
from reservation.models import Reservation

class ReservationCreateInputSerializer(serializers.ModelSerializer):
    client = serializers.IntegerField(required=True)
    car = serializers.IntegerField(required=True)
    
    class Meta:
        model = Reservation
        fields = ['client', 'car']

    def create(self, validated_data: dict):
        return Reservation.objects.create(
            client=validated_data.get('client'),
            car=validated_data.get('car'),
        )

class ReservationCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'