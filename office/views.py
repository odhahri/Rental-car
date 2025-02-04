from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet

from agent.serializers.agent_view_serializer import AgentSerializer
from agent.services.agent_service import AgentService
from cars.serializers.car_view_serializer import CarSerializer
from cars.services.car_service import CarService
from office.services.office_service import OfficeService
from client.serializers.client_view_serializer import ClientSerializer
from client.services.client_service import ClientService
from reservation.serializers.reservation_view_serializer import ReservationSerializer
from reservation.services.reservation_service import ReservationService

class OfficeViewSet(GenericViewSet):
    car_service = CarService()
    agent_service = AgentService()
    reservation_service = ReservationService()
    client_service = ClientService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_office_default_page(self, request):
        return render(request, 'office_default_page.html')

    def show_office_cars_page(self, request):
        cars_list = self.car_service.list()
        serializer = CarSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}
        context = {
            'table_title': 'Cars Management',
            'columns': columns,  # Add your car fields
            'items': cars_list,
            
            # Add your cars queryset
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'cars:add_car',  # URL name for adding a car
            'edit_url': 'cars:update_car', 
            'delete_url' : 'cars:delete_car',  # URL name for editing a car
            'column_types': column_types,
        }
        print('those are html types',column_types)
        return render(request, 'cars.html', context)
    
    def show_office_agents_page(self, request):
        agents_list = self.agent_service.list()
        serializer = AgentSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}

        context = {
            'table_title': 'Agents Management',
            'columns': columns,  # Add your car fields
            'items': agents_list,
            
            # Add your cars queryset
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'agents:add_agent',  # URL name for adding a car
            'edit_url': 'agents:update_agent', 
            'delete_url' : 'agents:delete_agent',  # URL name for editing a car
            'column_types': column_types,
        }
        print('those are html types',column_types)
        return render(request, 'agents.html', context)
    
    def show_office_reservations_page(self, request):
        reservations_list = self.reservation_service.list()
        serializer = ReservationSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}
        # Fields that requires dropdowns or modal selection 
        modalselect_fields = ['reservation_car_key', 'reservation_client_key']
        dropdown_fields = ['reservation_processed_by']
        column_types = {field: 'modalselect' if field in modalselect_fields else 'dropdown' if field in dropdown_fields else column_types[field] for field in columns}

        context = {
            'table_title': 'Reservation Management',
            'columns': columns,  # Add your car fields
            'items': reservations_list,
            
            # Add your cars queryset
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'reservations:add_reservation',  # URL name for adding a car
            'edit_url': 'reservations:update_reservation', 
            'delete_url' : 'reservations:delete_reservation',  # URL name for editing a car
            'column_types': column_types,
        }
        print('those are html types',column_types)
        return render(request, 'reservations.html', context)
    
    def show_office_clients_page(self, request):
        clients_list = self.client_service.list()
        serializer = ClientSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}
        column_types['user_blobs'] = 'file'
        context = {
            'table_title': 'Clients Management',
            'columns': columns,  # Add your car fields
            'items': clients_list,
            
            # Add your cars queryset
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'clients:add_client',  # URL name for adding a car
            'edit_url': 'clients:update_client', 
            'delete_url' : 'clients:delete_client',  # URL name for editing a car
            'column_types': column_types,
        }
        print('those are html types',column_types)
        return render(request, 'clients.html', context)