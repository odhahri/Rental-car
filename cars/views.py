from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from cars.models import Car
from common.shared.wrappers.rWrapper import ResponseWrapper
from .services.car_service import CarService
from cars.exceptions.exception_handler import CarServiceException

class CarViewSet(GenericViewSet):
    queryset = Car.objects.all()
    car_service = CarService()

    def create_car(self, request):
        try:
            data = self.car_service.create(request)
            return ResponseWrapper(data=data, message="Car created successfully.", success=True, status=201)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def list_cars(self, request):
        try:
            data = self.car_service.list()
            return ResponseWrapper(data=data, message="Cars retrieved successfully.", success=True, status=200)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def get_car(self, request, pk):
        try:
            data = self.car_service.get(pk)
            return ResponseWrapper(data=data, message="Car retrieved successfully.", success=True, status=200)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def update_car(self, request, pk):
        try:
            data = self.car_service.update(request, pk)
            return ResponseWrapper(data=data, message="Car updated successfully.", success=True, status=200)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def delete_car(self, request, pk):
        try:
            self.car_service.delete(pk)
            return ResponseWrapper(message="Car deleted successfully.", success=True, status=200)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def get_car_by_name(self, request, name):
        try:
            data = self.car_service.get_by_name(name)
            return ResponseWrapper(data=data, message="Car retrieved successfully.", success=True, status=200)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def list_car_with_availability(self, request, pk):
        try:
            data = self.car_service.list_car_with_availability(pk)
            return ResponseWrapper(data=data, message="Car availability retrieved successfully.", success=True, status=200)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    def add_blobs_by_id(self, request, pk):
        try:
            data = self.car_service.add_blobs_by_id(request, pk)
            return ResponseWrapper(data=data, message="Blobs added successfully.", success=True, status=201)
        except CarServiceException as e:
            return ResponseWrapper(message=e.message, success=False, status=e.status_code)

    # def get_blobs_by_id(self, request, pk, nature):
    #     try:
    #         data = self.car_service.get_blobs_by_id(pk, nature)
    #         if isinstance(data, dict):  # Handle no blobs case
    #             return ResponseWrapper(data=data, message="No blobs found.", success=False, status=404)
    #         zip_buffer = BytesIO()
    #         with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
    #             for i, blob in enumerate(data):
    #                 blob_data = blob['blob']
    #                 zip_file.writestr(f"blob_{i}.webp", blob_data)
    #         zip_buffer.seek(0)
    #         response = HttpResponse(zip_buffer, content_type='application/zip')
    #         response['Content-Disposition'] = f'attachment; filename="blobs_{pk}_{nature}.zip"'
    #         return response
    #     except CarServiceException as e:
    #         return ResponseWrapper(message=e.message, success=False, status=e.status_code)