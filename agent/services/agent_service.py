
from agent.models import Agent
from agent.serializers.agent_create_serializer import AgentCreateInputSerializer, AgentCreateOutputSerializer
from agent.serializers.agent_update_serializer import AgentUpdateSerializer
from agent.serializers.agent_view_serializer import AgentSerializer
class AgentService():
    def create(self, request):
        serializer = AgentCreateInputSerializer(data=request.data)
        print('those are agent data',request.data)
        serializer.is_valid(raise_exception=True)
        agent = serializer.save()
        output_serializer = AgentCreateOutputSerializer(agent)
        return output_serializer.data
    
    
    def list(self):
        agent = Agent.objects.all()
        serializer = AgentSerializer(agent, many=True)
        return serializer.data
    
    def get(self,pk):
        agent = Agent.objects.get(pk=pk)
        serializer = AgentSerializer(agent)
        # serializer.is_valid(raise_exception=True)
        return serializer.data
    
    def update(self,request,pk):
        agent = Agent.objects.get(pk=pk)
        serializer = AgentUpdateSerializer(instance = agent, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.validated_data
    
    def delete(self,pk):
        agent = Agent.objects.get(pk=pk)
        agent.delete()

    def get_by_name(self,name):
        agent = Agent.objects.get(name=name)
        serializer = AgentSerializer(agent)
        return serializer.validated_data
    
