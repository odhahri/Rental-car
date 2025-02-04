from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from common.models import UBlob  # Import your UBlob model

class UserCreateBlobSerializer(serializers.Serializer):
    user_images = serializers.ListField(child=serializers.CharField(), write_only=True)  # Array of base64-encoded images
    nature = serializers.CharField(default='photos')  # Default nature is 'photos'

    def __init__(self, *args, **kwargs):
        # Get the model class from the context
        self.model_class = kwargs.pop('model_class', None)
        super().__init__(*args, **kwargs)

        # Dynamically add the `user` field with the appropriate queryset
        if self.model_class:
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=self.model_class.objects.all())

    def create(self, validated_data):
        # Extract user_images and remove it from validated_data
        user_images = validated_data.pop('user_images')
        nature = validated_data.get('nature', 'photos')

        # Get the user instance (e.g., Agent, Client, etc.)
        user = validated_data['user']

        # Get the ContentType for the model class
        content_type = ContentType.objects.get_for_model(self.model_class)

        # Split each image into chunks and create UBlob instances
        blobs_to_create = []
        for image_index, user_image in enumerate(user_images):
            order = 0  # Initialize order for each image
            while len(user_image) > 0:
                # Take the first 500 characters
                chunk = user_image[:500]
                user_image = user_image[500:]  # Remove the processed chunk

                # Create a UBlob instance for the chunk
                blobs_to_create.append(
                    UBlob(
                        content_type=content_type,
                        object_id=user.pk,
                        blob=chunk,  # Store the chunk
                        nature=nature,
                        order=order,
                        image_id=f"image_{image_index}"  # Track which image this chunk belongs to
                    )
                )

                order += 1  # Increment order for the next chunk

        # Bulk create UBlob instances for performance
        return UBlob.objects.bulk_create(blobs_to_create)

    def to_representation(self, instance):
        # Customize the response output
        return {
            'blob_id': instance.blob_id,
            'user_id': instance.object_id,
            'nature': instance.nature,
            'order': instance.order,
            'image_id': instance.image_id  # Include image_id in the response
        }