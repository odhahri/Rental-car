from rest_framework import serializers
from common.models import UBlob
from common.shared.models.baseUser import BaseUser


class UserCreateBlobSerializer(serializers.Serializer):
    def get_user_queryset():
        queryset = []
        for subclass in BaseUser.__subclasses__():
            queryset.extend(subclass.objects.all())
        return queryset

    user = serializers.PrimaryKeyRelatedField(queryset=get_user_queryset())    
    user_images = serializers.ListField(
        child=serializers.CharField(max_length=5000),  # List of Base64 encoded blobs
        allow_empty=False
    )


    def create(self, validated_data):
        user = validated_data['user']
        blob_nature = validated_data['nature']
        user_images = validated_data['user_images']

        blobs_to_create = []
        for user_image in user_images:
            # Split if necessary
            while len(user_image) > 500:
                order = 0
                blobs_to_create.append(UBlob(user=user, blob=user_image[:500],nature=blob_nature,order=order))
                user_image = user_image[500:]
                order += 1
            blobs_to_create.append(UBlob(user=user, blob=user_image, nature=blob_nature, order=order))

        # Bulk create for performance
        return UBlob.objects.bulk_create(blobs_to_create)

# class UserUpdateBlobSerializer(serializers.Serializer):
#     # user_image = serializers.CharField(max_length=5000)  # For base64 image encoding

#     # def update(self, instance, validated_data):
#     #     instance.blob = validated_data.get('user_image', instance.blob)
#     #     instance.save()
#     #     return instance


    
# class UserViewBlobSerializer(serializers.Serializer):
#     user_blobs = serializers.CharField(max_length=5000)  # For base64 image encoding
#     user_id = serializers.IntegerField()
    