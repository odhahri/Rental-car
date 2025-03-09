

from rest_framework import serializers

class KekUserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    roles = serializers.ListField(child=serializers.CharField(max_length=50))
    password = serializers.CharField(max_length=100)
   
    
class KekUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=100)



    

