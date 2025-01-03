from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from client.services.client_service import ClientService

# rest framework django view 

from .models import Client

class ClientViewSet(GenericViewSet):

    queryset = Client.objects.all()
    client_service = ClientService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def create_client(self, request):
        client = self.client_service.create(request)
        return Response(data=client, status=201)
    
    def list_clients(self, request):
        clients = self.client_service.list()
        return Response(data=clients, status=200)
    
    def get_client(self, request, pk):
        client = self.client_service.get(pk)
        return Response(data=client, status=200)
    
    def update_client(self, request, pk):
        client = self.client_service.update(request, pk)
        return Response(data=client, status=200)
    

    def delete_client(self, request, pk):
        self.client_service.delete(pk)
        return Response(status=204)
    
    def get_client_by_name(self, request, pk):
        client = self.client_service.get_by_name(pk)
        return Response(data=client, status=200)
    
    def get_client_by_id(self, request, pk):
        client = self.client_service.get_by_id(pk)
        return Response(data=client, status=200)
    
    


