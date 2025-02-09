import zlib
from PIL import Image
from io import BytesIO
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from client.models import Client
from common.models import UBlob

class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='client_id')
    user_name = serializers.CharField(source='username')
    user_email = serializers.EmailField(source='email')
    user_first_name = serializers.CharField(source='fname')
    user_last_name = serializers.CharField(source='lname')
    user_phone_number = serializers.IntegerField(source='phone')
    user_identity = serializers.CharField(source='identity')
    user_created_at = serializers.DateTimeField(source='created_at')
    user_updated_at = serializers.DateTimeField(source='updated_at')
    # user_blobs = serializers.SerializerMethodField()  # Custom field for UBlob instances

    # def decompress_data(self, compressed_data, content_type):
    #     """
    #     Decompress binary data based on its content type.
    #     :param compressed_data: Compressed binary data.
    #     :param content_type: MIME type of the data (e.g., 'image/jpeg').
    #     :return: Decompressed binary data.
    #     """
    #     if content_type.startswith('image/'):
    #         # Decompress images using Pillow
    #         try:
    #             image = Image.open(BytesIO(compressed_data))
    #             output = BytesIO()
    #             image.save(output, format=image.format)  # Save in the original format
    #             return output.getvalue()
    #         except Exception as e:
    #             print(f"Image decompression failed: {e}")
    #             return compressed_data  # Return original data if decompression fails
    #     else:
    #         # Decompress non-image data using zlib
    #         try:
    #             return zlib.decompress(compressed_data)
    #         except zlib.error as e:
    #             print(f"Decompression failed: {e}")
    #             return compressed_data  # Return original data if decompression fails

    # def get_user_blobs(self, obj):
    #     # Get the ContentType for the Client model
    #     content_type = ContentType.objects.get_for_model(Client)

    #     # Filter UBlob instances for this Client
    #     ublobs = UBlob.objects.filter(content_type=content_type, object_id=obj.client_id)

    #     # Serialize the UBlob instances and decompress the data
    #     user_blobs = []
    #     for ublob in ublobs:
    #         # Decompress the binary data
    #         decompressed_data = self.decompress_data(ublob.blob, ublob.nature)

    #         # Append the decompressed data to the response
    #         user_blobs.append({
    #             'blob_id': ublob.blob_id,
    #             'blob': decompressed_data,  # Decompressed binary data
    #             'nature': ublob.nature,
    #         })

    #     return user_blobs