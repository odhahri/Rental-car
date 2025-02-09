from io import BytesIO
import zipfile
from django.http import HttpResponse
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
    


    def get_blobs_by_id_and_nature(self, request, pk, nature):
            blobs = self.client_service.get_blobs_by_id_and_nature(pk, nature)
            print('blobs are ',blobs)
            
            if blobs:
                # Create a ZIP file in memory
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for i, blob in enumerate(blobs):
                        blob_data = blob['blob']
                        zip_file.writestr(f"blob_{i}.webp", blob_data)  # Adjust the filename and extension as needed

                # Prepare the response
                zip_buffer.seek(0)
                response = HttpResponse(zip_buffer, content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename="blobs_{pk}_{nature}.zip"'
                return response
            else:
                return Response({"detail": "No blobs found."}, status=404)
    


    def add_blobs_by_id(self, request, pk):
        blobs = self.client_service.add_blobs_by_id(request, pk)
        return Response(data="Blobs added successfuly ! ", status=201)
