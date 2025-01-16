from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='car_id')  
    car_name = serializers.CharField(source='name')
    car_brand_name = serializers.CharField(source='brand')
    car_model_name = serializers.CharField(source='model')
    car_color = serializers.CharField(source='color')
    car_manufacture_year = serializers.IntegerField(source='year')
    car_rental_price = serializers.IntegerField(source='rentalprice')
    car_image = serializers.CharField(source='image')

   