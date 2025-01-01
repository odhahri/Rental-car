from rest_framework import serializers
from reservation.models import Reservation

class ReservationCreateInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'

    # def create(self, validated_data: dict):
    #     return Car.objects.create(
    #         name=validated_data.get('name'),
    #         color=validated_data.get('color'),
    #         year=validated_data.get('year'),
    #         price=validated_data.get('price'),
    #         image=validated_data.get('image')
    #     )

class ReservationCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'