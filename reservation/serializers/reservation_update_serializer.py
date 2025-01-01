from rest_framework import serializers
from reservation.models import Reservation

class ReservationUpdateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50,  required=False)
    color = serializers.CharField(max_length=50, required=False)
    year = serializers.CharField(max_length=50,  required=False)
    image = serializers.CharField(max_length=50, required=False)
    price = serializers.CharField(max_length=50, required=False)
    image = serializers.CharField(max_length=50, required=False)



    class Meta:
        model = Reservation
        fields = ['name', 'color', 'year', 'price', 'image']  

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.year = validated_data.get('year', instance.year)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)




        instance.save()
        return instance