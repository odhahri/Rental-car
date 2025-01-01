from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from cars.services.car_service import CarService
from django.shortcuts import render

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
        return Response(data=car, status=200)
    

    def delete_car(self, request, pk):
        self.car_service.delete(pk)
        return Response(status=204)
    
    def get_car_by_name(self, request, name):
        car = self.car_service.get_by_name(name)
        return Response(data=car, status=200)
    

     # HTML-based Views
    def car_list_page(self, request):
        cars = self.car_service.list()
        return render(request, 'cars/car_list.html', {'cars': cars})

    def car_detail_page(self, request, pk):
        car = self.car_service.get(pk)
        return render(request, 'cars/car_detail.html', {'car': car})

