
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
        client_output_serializer = ClientCreateOutputSerializer(client)

        # Handle binary files from request.FILES
        if 'user_blobs' in request.FILES:
            user_blobs = request.FILES.getlist('user_blobs')  # Get list of uploaded files
            blob_data = {
                'user': client_output_serializer.data['id'],  # Pass client.id to the blob
                'user_images': user_blobs,  # Pass the list of binary files
                'nature': 'photos'  # Set nature to 'photos'
            }

            # Serialize and save the binary files
            userBlobSerializer = UserCreateBlobSerializer(data=blob_data, model_class=Client)
            userBlobSerializer.is_valid(raise_exception=True)
            ublobs = userBlobSerializer.save()
        # if identity images were passed, store them in ublob table with nature as 'identity'
        # identity_data = {
        # 'user': client_output_serializer.data['id'], 
        # 'user_images': request.data.get('user_identity'),  
        # 'nature': 'identity'  
        # }
        # userIdentitySerializer = UserCreateBlobSerializer(data=identity_data, model_class=Client)
        # userIdentitySerializer.is_valid(raise_exception=True)
        # uIdentity = userIdentitySerializer.save()
        # return client_output_serializer.data
    
    
    def list(self):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return serializer.data
    
    def get(self,pk):
        client = Client.objects.get(pk=pk)
        serializer = ClientSerializer(client)
        return serializer.data
    
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
    
