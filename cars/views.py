import base64
from io import BytesIO
import zipfile
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from cars.services.car_service import CarService
from django.shortcuts import render
import base64


# rest framework django view 

from .models import Car

class CarViewSet(GenericViewSet):

    queryset = Car.objects.all()
    car_service = CarService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def create_car(self, request):
        car = self.car_service.create(request)
        return Response(data=car, status=201)
    
    def list_cars(self, request):
        cars = self.car_service.list()
        return Response(data=cars, status=200)
    
    def get_car(self, request, pk):
        car = self.car_service.get(pk)
        return Response(data=car, status=200)
    
    def update_car(self, request, pk):
        car = self.car_service.update(request, pk)
        return Response(data='car updated successfully', status=200)
    

    def delete_car(self, request, pk):
        try:
            self.car_service.delete(pk)
            return Response(data='Car deleted successfully', status=200)
        except Car.DoesNotExist:
            return Response(data ='Car does not exists', status=204)
    
    def get_car_by_name(self, request, name):
        car = self.car_service.get_by_name(name)
        return Response(data=car, status=200)
    
    def list_car_with_availability(self, request, pk):
        print('pk is ',pk)
        cars = self.car_service.list_car_with_availability(pk)
        return Response(data=cars, status=200)
    

     # HTML-based Views

    def car_list_page(self, request):
        cars = self.car_service.list()
        
        for car in cars:
            print (car['id'])
            blobs = self.car_service.get_blobs_by_id(car['id'], "image")  # Fetch blobs for each car
            if blobs:
                blob_data = blobs[0]['blob']  # Get the first blob (binary)
                encoded_image = base64.b64encode(blob_data).decode('utf-8')  # Convert to Base64 string
                car['image_url'] = f"data:image/webp;base64,{encoded_image}"  # Embed in HTML-friendly format
            else:
                car['image_url']= None  # Fallback if no image is available

        return render(request, 'cars/car_list.html', {'cars': cars})


    def car_detail_page(self, request, pk):
        car = self.car_service.get(pk)  # Fetch car details
        blobs = self.car_service.get_blobs_by_id(pk, "image")  # Fetch images

        images = []
        for blob in blobs:
            encoded_image = base64.b64encode(blob['blob']).decode('utf-8')
            images.append(f"data:image/webp;base64,{encoded_image}")

        car['images'] = images  # Attach images to car object
        reservations = self.car_service.list_car_with_availability(pk)
        print('reservations are ',reservations)

        return render(request, 'cars/car_detail.html', {'car': car,'reservations': reservations})

    def add_blobs_by_id(self, request, pk):
        blobs = self.car_service.add_blobs_by_id(request, pk)
        return Response(data="Blobs added successfuly ! ", status=201)
    
    def get_blobs_by_id(self, request, pk, nature):
        blobs = self.car_service.get_blobs_by_id(pk, nature)
        print('blobs are ',blobs)
            
        if blobs:
            # Create a ZIP file in memory
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for i, blob in enumerate(blobs):
                    blob_data = blob['blob']
                    zip_file.writestr(f"blob_{i}.webp", blob_data)  # Adjust the filename and extension as needed

            # Prepare the response
            zip_buffer.seek(0)
            response = HttpResponse(zip_buffer, content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="blobs_{pk}_{nature}.zip"'
            return response
        else:
            return Response({"detail": "No blobs found."}, status=404)