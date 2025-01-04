from rest_framework import serializers
from cars.models import Car

class CarCreateInputSerializer(serializers.Serializer):
    # image = serializers.CharField(max_length=50, required=True, allow_blank=True)

    brand_name = serializers.CharField(max_length=200, required=True)
    model_name = serializers.CharField(max_length=100, required=True)
    car_name = serializers.CharField(max_length=100, required=True)
    car_color = serializers.CharField(max_length=100, required=True)
    manufacture_year = serializers.IntegerField(required=True)
    rental_price = serializers.IntegerField(required=True)
    car_image = serializers.CharField(max_length=500, required=False, allow_blank=True)


    def create(self, validated_data):
        return Car.objects.create(
            brand=validated_data.get('brand_name'),
            model=validated_data.get('model_name'),
            name=validated_data.get('car_name'),
            color=validated_data.get('car_color'),
            year=validated_data.get('manufacture_year'),
            rentalprice=validated_data.get('rental_price'),
            image=validated_data.get('car_image')
        )
class CarCreateOutputSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    brand_name = serializers.CharField(source='brand')
    model_name = serializers.CharField(source='model')
    car_name = serializers.CharField(source='name')
    car_color = serializers.CharField(source='color')
    manufacture_year = serializers.IntegerField(source='year')
    rental_price = serializers.IntegerField(source='rentalprice')
    car_image = serializers.CharField(source='image', allow_blank=True, required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Car
        fields = ['car_id', 'brand_name', 'model_name', 'car_name', 'car_color', 'manufacture_year', 'rental_price', 'car_image', 'created_at', 'updated_at']