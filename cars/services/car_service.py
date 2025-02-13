
from cars.models import Car
from cars.serializers.car_create_serializer import CarCreateInputSerializer, CarCreateOutputSerializer
from cars.serializers.car_update_serializer import CarUpdateSerializer
from cars.serializers.car_view_serializer import CarSerializer
from common.models import CBlob
from common.shared.serializers.user_blob_serializer import CarBlobSerializer, CarCreateBlobSerializer
from reservation.models import Reservation
from reservation.serializers.reservation_view_serializer import ReservationSerializer
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
        serializer = CarUpdateSerializer(instance = car, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.validated_data

    
    def delete(self,pk):
            car = Car.objects.get(pk=pk)
            car.delete()

    def get_by_name(self,name):
        car = Car.objects.get(name=name)
        serializer = CarSerializer(car)
        return serializer.validated_data
    
    def add_blobs_by_id(self,request,pk):
        car = Car.objects.get(pk=pk)

       
        blob_photo_data = {
            'car_images': request.FILES.getlist('photo'),
            'nature': 'photo',
            'car': car.car_id
        }
        serializer = CarCreateBlobSerializer( data = blob_photo_data)
        serializer.is_valid(raise_exception=True)
        carblob = serializer.save()
        carBlobSerializer = CarBlobSerializer(carblob, many=True)

        
        return carBlobSerializer.data
    
    def get_blobs_by_id(self,pk,nature):
        carblob = CBlob.objects.filter(car = pk)
        serializer = CarBlobSerializer(carblob, many=True)
        return serializer.data
    

    def list_car_with_availability(self,pk):
        # list cars with corresponding availability. 
        print('pk is ',pk)
        # car = Car.objects.get(car_id=pk)
        reservations = Reservation.objects.filter(car = pk, status = 'APPROVED')
        if reservations.exists():
            serializer =  ReservationSerializer(reservations, many=True)
            return serializer.data
        else :
            return 'No current reservations found for this car'


        
