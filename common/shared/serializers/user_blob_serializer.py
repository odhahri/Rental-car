import zlib  # For general binary data compression
from PIL import Image  # For image compression
from io import BytesIO  # For in-memory binary streams
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from common.models import UBlob  # Import your UBlob model

class UserCreateBlobSerializer(serializers.Serializer):
    user_images = serializers.ListField(
        child=serializers.FileField(),  # Use FileField for binary files
        write_only=True
    )
    nature = serializers.CharField(default='photos')  # Default nature is 'photos'

    def __init__(self, *args, **kwargs):
        # Get the model class from the context
        self.model_class = kwargs.pop('model_class', None)
        super().__init__(*args, **kwargs)

        # Dynamically add the `user` field with the appropriate queryset
        if self.model_class:
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=self.model_class.objects.all())

    def compress_image(self, binary_data, format='WEBP', quality=85):
        """
        Compress an image using Pillow.
        :param binary_data: Binary data of the image.
        :param format: Output format (e.g., 'WEBP', 'JPEG').
        :param quality: Compression quality (0-100).
        :return: Compressed binary data.
        """
        try:
            image = Image.open(BytesIO(binary_data))
            output = BytesIO()
            image.save(output, format=format, quality=quality)  # Compress the image
            return output.getvalue()
        except Exception as e:
            print(f"Image compression failed: {e}")
            return binary_data  # Return original data if compression fails

    def compress_data(self, binary_data, content_type):
        """
        Compress binary data based on its content type.
        :param binary_data: Binary data to compress.
        :param content_type: MIME type of the data (e.g., 'image/jpeg').
        :return: Compressed binary data.
        """
        if content_type.startswith('image/'):
            # Compress images using Pillow
            return self.compress_image(binary_data, format='WEBP', quality=85)
        else:
            # Compress non-image data using zlib
            return zlib.compress(binary_data, level=9)

    def create(self, validated_data):
        # Extract user_images and remove it from validated_data
        user_images = validated_data.pop('user_images')
        nature = validated_data.get('nature', 'photos')

        # Get the user instance (e.g., Agent, Client, etc.)
        user = validated_data['user']

        # Get the ContentType for the model class
        content_type = ContentType.objects.get_for_model(self.model_class)

        # Create UBlob instances for each uploaded file
        blobs_to_create = []
        for image_index, user_image in enumerate(user_images):
            # Read the binary data from the uploaded file
            binary_data = user_image.read()

            # Get the MIME type of the file
            file_content_type = user_image.content_type

            # Compress the binary data based on its content type
            compressed_data = self.compress_data(binary_data, file_content_type)

            # Create a UBlob instance for the compressed binary data
            blobs_to_create.append(
                UBlob(
                    content_type=content_type,
                    object_id=user.pk,
                    blob=compressed_data,  # Store the compressed binary data
                    nature=nature,
                    order=image_index,  # Use image_index as the order
                    image_id=f"image_{image_index}"  # Track which image this blob belongs to
                )
            )

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