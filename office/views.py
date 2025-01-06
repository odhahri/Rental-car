from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet

from cars.serializers.car_view_serializer import CarSerializer
from cars.services.car_service import CarService

class OfficeViewSet(GenericViewSet):
    car_service = CarService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_office_default_page(self, request):
        return render(request, 'office_default_page.html')

    def show_office_cars_page(self, request):
        cars_list = self.car_service.list()
        serializer = CarSerializer()
        columns = [field for field in serializer.fields]

        context = {
            'table_title': 'Cars Management',
            'columns': columns,  # Add your car fields
            'items': cars_list,  # Add your cars queryset
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'add_car',  # URL name for adding a car
            'view_url': 'car_detail',  # URL name for viewing a car
            'edit_url': 'edit_car',  # URL name for editing a car
        }
        print('carss columns is :',context['items']) 
        return render(request, 'cars.html', context)

    def show_office_agents_page(self, request):
        return render(request, 'agents.html')
    
    def show_office_reservations_page(self, request):
        return render(request, 'reservations.html')
    
    def show_office_clients_page(self, request):
        return render(request, 'clients.html')