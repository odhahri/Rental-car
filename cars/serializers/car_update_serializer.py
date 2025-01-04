from rest_framework import serializers
from cars.models import Car

class CarUpdateSerializer(serializers.Serializer):
    brand_name = serializers.CharField(max_length=200, required=False)
    model_name = serializers.CharField(max_length=100, required=False)
    car_name = serializers.CharField(max_length=100, required=False)
    car_color = serializers.CharField(max_length=100, required=False)
    manufacture_year = serializers.IntegerField(required=False)
    rental_price = serializers.IntegerField(required=False)
    car_image = serializers.CharField(max_length=500, required=False, allow_blank=True)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand_name', instance.brand)
        instance.model = validated_data.get('model_name', instance.model)
        instance.name = validated_data.get('car_name', instance.name)
        instance.color = validated_data.get('car_color', instance.color)
        instance.year = validated_data.get('manufacture_year', instance.year)
        instance.rentalprice = validated_data.get('rental_price', instance.rentalprice)
        instance.image = validated_data.get('car_image', instance.image)
        instance.save()
        return instance
    
