
from client.models import Client
from client.serializers.client_create_serializer import  ClientCreateInputSerializer, ClientCreateOutputSerializer 
from client.serializers.client_update_serializer import ClientUpdateSerializer
from client.serializers.client_view_serializer import ClientSerializer
from common.shared.serializers.user_blob_serializer import UserCreateBlobSerializer


class ClientService():
    def create(self, request):
        serializer = ClientCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()
        output_serializer = ClientCreateOutputSerializer(client)

        print('output_serializer',output_serializer.data)
        blob_data = {
        'user': Client.objects.get(pk=output_serializer.id),  # Pass client.id to the blob
        'user_images': request.data.get('user_images'),  # Pass user_image data
        'nature': 'photos'  # Pass nature of the blob
    }
        
        userBlobSerializer = UserCreateBlobSerializer(data=blob_data)
        userBlobSerializer.is_valid(raise_exception=True)
        userBlobSerializer.save()
        return output_serializer.data
    
    
    def list(self):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return serializer.data
    
    def get(self,pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
    
    def update(self,request,pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientUpdateSerializer(instance=client, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.validated_data
    
    def delete(self,pk):
        client = Client.objects.get(pk=pk)
        client.delete()

    def get_by_name(self,name):
        client = Client.objects.get(name=name)
        serializer = ClientSerializer(client)
        return serializer.validated_data
    
    def get_by_id(self,id):
        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client)
        return serializer.validated_data
    
