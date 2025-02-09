
from agent.models import Agent
from agent.serializers.agent_create_serializer import AgentCreateInputSerializer, AgentCreateOutputSerializer
from agent.serializers.agent_update_serializer import AgentUpdateSerializer
from agent.serializers.agent_view_serializer import AgentSerializer
from django.contrib.contenttypes.models import ContentType
from common.models import UBlob
from common.shared.serializers.user_blob_serializer import UserBlobSerializer, UserCreateBlobSerializer

class AgentService():
    def create(self, request):
        serializer = AgentCreateInputSerializer(data=request.data)
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
    

    def get_blobs_by_id_and_nature(self,id,nature):
        blobs = UBlob.objects.filter(content_type = ContentType.objects.get_for_model(Agent), object_id=id,nature=nature)
        blobs_serializer = UserBlobSerializer(blobs, many=True)
        return blobs_serializer.data
    
    def add_blobs_by_id(self,request,pk):
        agent = Agent.objects.get(pk=pk)
        blob_photo_data = {
            'user': agent.agent_id,
            'user_images': request.FILES.getlist('photo'),
            'nature': 'photo'
        }
        userBlobPhotoSerializer = UserCreateBlobSerializer(data=blob_photo_data, model_class=Agent)
        userBlobPhotoSerializer.is_valid(raise_exception=True)
        uphotoblobs = userBlobPhotoSerializer.save()
        userBlobSerializer = UserBlobSerializer(uphotoblobs, many=True)
        return userBlobSerializer.data