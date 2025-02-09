from rest_framework import serializers
from cars.models import Car

class CarCreateInputSerializer(serializers.Serializer):
    
    car_brand_name = serializers.CharField(max_length=50, required=True)
    car_model_name = serializers.CharField(max_length=50, required=True)
    car_name = serializers.CharField(max_length=50, required=True)
    car_color = serializers.CharField(max_length=50, required=True)
    car_manufacture_year = serializers.IntegerField(required=True)
    car_rental_price = serializers.IntegerField(required=True)
    

    def create(self, validated_data):
        return Car.objects.create(
            brand=validated_data.get('car_brand_name'),
            model=validated_data.get('car_model_name'),
            name=validated_data.get('car_name'),
            color=validated_data.get('car_color'),
            year=validated_data.get('car_manufacture_year'),
            rentalprice=validated_data.get('car_rental_price'),
        )
class CarCreateOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='car_id')
    car_brand_name = serializers.CharField(source='brand')
    car_model_name = serializers.CharField(source='model')
    car_name = serializers.CharField(source='name')
    car_color = serializers.CharField(source='color')
    car_manufacture_year = serializers.IntegerField(source='year')
    car_rental_price = serializers.IntegerField(source='rentalprice')
    car_created_at = serializers.DateTimeField(source='created_at')
    car_updated_at = serializers.DateTimeField(source='updated_at')


