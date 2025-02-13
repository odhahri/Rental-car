from django.shortcuts import render


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
            'columns': columns,  
            'items': cars_list,
            'can_have_blobs': True,
            'possible_blob_natures': ['photo'],
            'add_blob_url': 'cars:add_blobs_by_id',
            'get_blobs_url': 'cars:get_blobs_by_id',
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'cars:add_car',  
            'edit_url': 'cars:update_car', 
            'delete_url' : 'cars:delete_car', 
            'column_types': column_types,
        }
        return render(request, 'cars.html', context)
    
    def show_office_agents_page(self, request):
        agents_list = self.agent_service.list()
        serializer = AgentSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}

        context = {
            'table_title': 'Agents Management',
            'columns': columns,  
            'items': agents_list,
            'can_have_blobs': True,
            'possible_blob_natures': ['photo'],
            'add_blob_url': 'agents:add_blobs_by_id',
            'get_blobs_url': 'agents:get_blobs_by_id_and_nature',
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'agents:add_agent',  
            'edit_url': 'agents:update_agent', 
            'delete_url' : 'agents:delete_agent',  
            'column_types': column_types,
        }
        return render(request, 'agents.html', context)
    
    def show_office_reservations_page(self, request):
        reservations_list = self.reservation_service.list()
        serializer = ReservationSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}
        search_dropdown_fields = ['reservation_car_key', 'reservation_client_key', 'reservation_processed_by']
        simple_dropdown_fields = ['reservation_status']
        # column_types = {field: 'dropdown-search' if field in search_dropdown_fields else column_types[field] for field in columns}
        column_types = {field: 'dropdown-search' if field in search_dropdown_fields else 'dropdown-simple' if field in simple_dropdown_fields else column_types[field] for field in columns}
        clients = self.client_service.list()  
        cars = self.car_service.list()  
        agents = self.agent_service.list()
        dropdown_data = {
            'reservation_client_key': clients,
            'reservation_car_key': cars,
            'reservation_processed_by': agents,
            'reservation_status': ['PENDING', 'APPROVED', 'REJECTED'],
        }
        toshow = {
            'reservation_client_key': ['id', 'user_name'], 
            'reservation_car_key': ['id', 'car_name'], 
            'reservation_processed_by': ['id', 'user_name'],
        }
        hover_dropdown_fields_url = [{'reservation_car_key':'cars:list_car_availability'}]
        context = {
            'table_title': 'Reservation Management',
            'columns': columns,  
            'items': reservations_list,
            'can_have_blobs': False,
            'possible_blob_natures': [],
            'add_blob_url': 'null',
            'get_blobs_url': 'null',
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'reservations:add_reservation',  
            'edit_url': 'reservations:update_reservation', 
            'delete_url' : 'reservations:delete_reservation', 
            'column_types': column_types,
            'dropdown_data': dropdown_data,
            'toshow' : toshow  ,
            'hover_dropdown_fields_url': hover_dropdown_fields_url,
            'car_availability_url':'cars:list_car_with_availability',
        }
        return render(request, 'reservations.html', context)
    
    def show_office_clients_page(self, request):
        clients_list = self.client_service.list()
        serializer = ClientSerializer()
        columns = [field for field in serializer.fields]
        column_types = {field: OfficeService.get_html_input_type(serializer.fields[field]) for field in columns}
        context = {
            'table_title': 'Clients Management',
            'columns': columns,  
            'items': clients_list,
            'can_have_blobs': True,
            'possible_blob_natures': ['photo', 'identity'],
            'add_blob_url': 'clients:add_blobs_by_id',
            'get_blobs_url': 'clients:get_blobs_by_id_and_nature',
            'show_actions': True,
            'show_add_button': True,
            'add_url': 'clients:add_client',  
            'edit_url': 'clients:update_client', 
            'delete_url' : 'clients:delete_client',  
            'column_types': column_types,
        }
        return render(request, 'clients.html', context)