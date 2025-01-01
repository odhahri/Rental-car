
from cars.models import Car
from cars.serializers.car_create_serializer import CarCreateInputSerializer, CarCreateOutputSerializer
from cars.serializers.car_update_serializer import CarUpdateSerializer
from cars.serializers.car_view_serializer import CarSerializer
class CarService():
    def create(self, request):
        serializer = CarCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        output_serializer = CarCreateOutputSerializer(car)
        return output_serializer.data
    
    
    def list(self):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return serializer.data
    
    def get(self,pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
        # serializer.is_valid(raise_exception=True)
        return serializer.data
    
    def update(self,request,pk):
        car = Car.objects.get(pk=pk)
        serializer = CarCreateInputSerializer(instance=car,data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        outputserializer = CarUpdateSerializer(car)
        # outputserializer.is_valid(raise_exception=True)
        return outputserializer.data
    
    def delete(self,pk):
        car = Car.objects.get(pk=pk)
        car.delete()

    def get_by_name(self,name):
        car = Car.objects.get(name=name)
        serializer = CarSerializer(car)
        return serializer.validated_data
    
