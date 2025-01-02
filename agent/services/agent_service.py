
from agent.models import Agent
from agent.serializers.agent_create_serializer import agentCreateInputSerializer, agentCreateOutputSerializer
from agent.serializers.agent_update_serializer import agentUpdateSerializer
from agent.serializers.agent_view_serializer import agenterializer
class Agentervice():
    def create(self, request):
        serializer = agentCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        agent = serializer.save()
        output_serializer = agentCreateOutputSerializer(agent)
        return output_serializer.data
    
    
    def list(self):
        agent = agent.objects.all()
        serializer = agenterializer(agent, many=True)
        return serializer.data
    
    def get(self,pk):
        agent = agent.objects.get(pk=pk)
        serializer = agenterializer(agent)
        # serializer.is_valid(raise_exception=True)
        return serializer.data
    
    def update(self,request,pk):
        agent = Agent.objects.get(pk=pk)
        serializer = agentCreateInputSerializer(instance=agent,data=request.data)
        serializer.is_valid(raise_exception=True)
        agent = serializer.save()
        outputserializer = agentUpdateSerializer(agent)
        # outputserializer.is_valid(raise_exception=True)
        return outputserializer.data
    
    def delete(self,pk):
        agent = agent.objects.get(pk=pk)
        agent.delete()

    def get_by_name(self,name):
        agent = agent.objects.get(name=name)
        serializer = agenterializer(agent)
        return serializer.validated_data
    
