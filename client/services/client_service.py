
from client.models import client
from client.serializers.client_create_serializer import ClientCreateInputSerializer, ClientCreateOutputSerializer 
from client.serializers.client_update_serializer import ClientUpdateSerializer
from client.serializers.client_view_serializer import ClientSerializer

class ClientService():
    def create(self, request):
        serializer = ClientCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()
        output_serializer = ClientCreateOutputSerializer(client)
        return output_serializer.data
    
    
    def list(self):
        clients = client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
    
    def get(self,pk):
        client = client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
    
    def update(self,request,pk):
        client = client.objects.get(pk=pk)
        serializer = ClientUpdateSerializer(instance=client, data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()
    
    def delete(self,pk):
        client = client.objects.get(pk=pk)
        client.delete()

    def get_by_name(self,name):
        client = client.objects.get(name=name)
        serializer = ClientSerializer(client)
        return serializer.validated_data
    
    def get_by_id(self,id):
        client = client.objects.get(id=id)
        serializer = ClientSerializer(client)
        return serializer.validated_data
    
