from rest_framework import serializers
from cars.models import Car

class CarCreateInputSerializer(serializers.ModelSerializer):
    # image = serializers.CharField(max_length=50, required=True, allow_blank=True)

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data: dict):
        return Car.objects.create(
            name=validated_data.get('name'),
            color=validated_data.get('color'),
            year=validated_data.get('year'),
            price=validated_data.get('price'),
            image=validated_data.get('image')
        )

class CarCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'