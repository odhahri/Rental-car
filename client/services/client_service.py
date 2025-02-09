
from client.models import Client
from client.serializers.client_create_serializer import  ClientCreateInputSerializer, ClientCreateOutputSerializer 
from client.serializers.client_update_serializer import ClientUpdateSerializer
from client.serializers.client_view_serializer import ClientSerializer
from common.models import UBlob
from common.shared.serializers.user_blob_serializer import UserBlobSerializer, UserCreateBlobSerializer
from django.contrib.contenttypes.models import ContentType


class ClientService():
    def create(self, request):
        serializer = ClientCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()
        client_output_serializer = ClientCreateOutputSerializer(client)
        return client_output_serializer.data
    
    
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
    
    def get_blobs_by_id_and_nature(self,id,nature):
        blobs = UBlob.objects.filter(content_type = ContentType.objects.get_for_model(Client), object_id=id,nature=nature)
        blobs_serializer = UserBlobSerializer(blobs, many=True)
        return blobs_serializer.data
    
    def add_blobs_by_id(self,request,pk):
        client = Client.objects.get(pk=pk)
        blob_identity_data = {
            'user': client.client_id,
            'user_images': request.FILES.getlist('identity'),
            'nature': 'identity'
        }
        blob_photo_data = {
            'user': client.client_id,
            'user_images': request.FILES.getlist('photo'),
            'nature': 'photo'
        }
        userBlobIdentitySerializer = UserCreateBlobSerializer(data=blob_identity_data, model_class=Client)
        userBlobIdentitySerializer.is_valid(raise_exception=True)
        uidentityblobs = userBlobIdentitySerializer.save()
        userBlobPhotoSerializer = UserCreateBlobSerializer(data=blob_photo_data, model_class=Client)
        userBlobPhotoSerializer.is_valid(raise_exception=True)
        uphotoblobs = userBlobPhotoSerializer.save()
        userBlobSerializer = UserBlobSerializer(uidentityblobs, many=True)
        return userBlobSerializer.data