
from client.models import Client
from client.serializers.client_create_serializer import ClientCreateBlobSerializer, ClientCreateInputSerializer, ClientCreateOutputSerializer 
from client.serializers.client_update_serializer import ClientUpdateSerializer
from client.serializers.client_view_serializer import ClientSerializer

class ClientService():
    def create(self, request):

        
        serializer = ClientCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()
        output_serializer = ClientCreateOutputSerializer(client)
        print('output_serializer',output_serializer.data)
        # i would like to take the id from the outputserilizer and combine it with user_image from the request data and pass them to the blob serializer 
        blob_data = {
        'id': client.client_id,  # Pass client.id to the blob
        'user_image': request.data.get('user_image')  # Pass user_image data
    }
        blobserializer = ClientCreateBlobSerializer(data=blob_data)
        blobserializer.is_valid(raise_exception=True)
        blob = blobserializer.save()
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
    
