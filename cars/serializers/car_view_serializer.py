from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='car_id', read_only=True)  
    car_name = serializers.CharField(source='name')
    brand_name = serializers.CharField(source='brand')
    model_name = serializers.CharField(source='model')
    car_color = serializers.CharField(source='color')
    manufacture_year = serializers.IntegerField(source='year')
    rental_price = serializers.IntegerField(source='rentalprice')
    car_image = serializers.CharField(source='image', allow_blank=True, required=False)

    class Meta:
        model = Car
        fields = [
            'id',        # Keep the primary key as is
            'car_name',
            'brand_name',
            'model_name',
            'car_color',
            'manufacture_year',
            'rental_price',
            'car_image'
        ]