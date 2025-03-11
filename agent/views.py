from io import BytesIO
import zipfile
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from agent.services.agent_service import AgentService
from common.shared.keycloak.constants import keycloak_scopes_resources
from .models import Agent

class AgentViewSet(GenericViewSet):
    keycloak_resources_scopes = keycloak_scopes_resources.keycloak_scopes_resources['agent']

    queryset = Agent.objects.all()
    agent_service = AgentService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def create_agent(self, request):
        agent = self.agent_service.create(request)
        return Response(data=agent, status=201)
    
    def list_agents(self, request):
        agents = self.agent_service.list()
        return Response(data=agents, status=200)
    
    def get_agent(self, request, pk):
        agent = self.agent_service.get(pk)
        return Response(data=agent, status=200)
    
    def update_agent(self, request, pk):
        agent = self.agent_service.update(request, pk)
        return Response(data=agent, status=200)
    

    def delete_agent(self, request, pk):
        self.agent_service.delete(pk)
        return Response(status=204)
    
    def get_agent_by_name(self, request, name):
        agent = self.agent_service.get_by_name(name)
        return Response(data=agent, status=200)
    
    def get_blobs_by_id(self, request, pk, nature):
            blobs = self.agent_service.get_blobs_by_id_and_nature(pk, nature)
            if blobs:
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for i, blob in enumerate(blobs):
                        blob_data = blob['blob']
                        zip_file.writestr(f"blob_{i}.webp", blob_data)  
                zip_buffer.seek(0)
                response = HttpResponse(zip_buffer, content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename="blobs_{pk}_{nature}.zip"'
                return response
            else:
                return Response({"detail": "No blobs found."}, status=404)
    

    def add_blobs_by_id(self, request, pk):
        blobs = self.agent_service.add_blobs_by_id(request, pk)
        return Response(data="Blobs added successfuly ! ", status=201)


