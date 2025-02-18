# services/car_service.py
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from cars.models import Car
from cars.serializers.car_create_serializer import CarCreateInputSerializer, CarCreateOutputSerializer
from cars.serializers.car_update_serializer import CarUpdateSerializer
from cars.serializers.car_view_serializer import CarSerializer
from common.models import CBlob
from common.shared.serializers.user_blob_serializer import CarBlobSerializer, CarCreateBlobSerializer
from reservation.models import Reservation
from reservation.serializers.reservation_view_serializer import ReservationSerializer
from cars.exceptions.exception_handler import CarNotFoundException, BlobNotFoundException, CarServiceException, ValidationException

class CarService:
    @transaction.atomic
    def create(self, request):
        try:
            serializer = CarCreateInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            car = serializer.save()
            output_serializer = CarCreateOutputSerializer(car)
            return output_serializer.data
        except ValidationError as e:
            raise ValidationException(message=str(e))

    def list(self):
        try:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return serializer.data
        except Exception as e:
            raise CarServiceException(message=str(e))

    def get(self, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return serializer.data
        except ObjectDoesNotExist:
            raise CarNotFoundException()

    @transaction.atomic
    def update(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarUpdateSerializer(instance=car, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.validated_data
        except ObjectDoesNotExist:
            raise CarNotFoundException()
        except ValidationError as e:
            raise ValidationException(message=str(e))

    @transaction.atomic
    def delete(self, pk):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
        except ObjectDoesNotExist:
            raise CarNotFoundException()

    def get_by_name(self, name):
        try:
            car = Car.objects.get(name=name)
            serializer = CarSerializer(car)
            return serializer.data
        except ObjectDoesNotExist:
            raise CarNotFoundException()

    @transaction.atomic
    def add_blobs_by_id(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            blob_photo_data = {
                'car_images': request.FILES.getlist('photo'),
                'nature': 'photo',
                'car': car.car_id
            }
            serializer = CarCreateBlobSerializer(data=blob_photo_data)
            serializer.is_valid(raise_exception=True)
            carblob = serializer.save()
            carBlobSerializer = CarBlobSerializer(carblob, many=True)
            return carBlobSerializer.data
        except ObjectDoesNotExist:
            raise CarNotFoundException()
        except ValidationError as e:
            raise ValidationException(message=str(e))

    def get_blobs_by_id(self, pk, nature):
        try:
            carblob = CBlob.objects.filter(car=pk, nature=nature)
            if not carblob.exists():
                raise BlobNotFoundException()
            serializer = CarBlobSerializer(carblob, many=True)
            return serializer.data
        except Exception as e:
            raise CarServiceException(message=str(e))

    def list_car_with_availability(self, pk):
        try:
            reservations = Reservation.objects.filter(car=pk, status='APPROVED')
            if not reservations.exists():
                return {"detail": "No current reservations found for this car."}
            serializer = ReservationSerializer(reservations, many=True)
            return serializer.data
        except Exception as e:
            raise CarServiceException(message=str(e))