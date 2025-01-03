from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from agent.services.agent_service import AgentService
from django.shortcuts import render

# rest framework django view 

from .models import agent

class AgentViewSet(GenericViewSet):

    queryset = agent.objects.all()
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
    

