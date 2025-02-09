from rest_framework import serializers

class CarUpdateSerializer(serializers.Serializer):
    car_brand_name = serializers.CharField(max_length=50, required=True)
    car_model_name = serializers.CharField(max_length=50, required=True)
    car_name = serializers.CharField(max_length=50, required=True)
    car_color = serializers.CharField(max_length=50, required=True)
    car_manufacture_year = serializers.IntegerField(required=True)
    car_rental_price = serializers.IntegerField(required=True)
    

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('car_brand_name', instance.brand)
        instance.model = validated_data.get('car_model_name', instance.model)
        instance.name = validated_data.get('car_name', instance.name)
        instance.color = validated_data.get('car_color', instance.color)
        instance.year = validated_data.get('car_manufacture_year', instance.year)
        instance.rentalprice = validated_data.get('car_rental_price', instance.rentalprice)
        instance.save()
        return instance
    
