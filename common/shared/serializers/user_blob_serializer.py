import zlib 
from PIL import Image  
from io import BytesIO  
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from cars.models import Car
from common.models import CBlob, UBlob  

class UserCreateBlobSerializer(serializers.Serializer):
    user_images = serializers.ListField(
        child=serializers.FileField(),  # Use FileField for binary files
        write_only=True
    )
    nature = serializers.CharField(default='photos')  

    def __init__(self, *args, **kwargs):
        self.model_class = kwargs.pop('model_class', None)
        super().__init__(*args, **kwargs)

        if self.model_class:
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=self.model_class.objects.all())

    def compress_image(self, binary_data, format='WEBP', quality=85):
      
        try:
            image = Image.open(BytesIO(binary_data))
            output = BytesIO()
            image.save(output, format=format, quality=quality)  
            return output.getvalue()
        except Exception as e:
            print(f"Image compression failed: {e}")
            return binary_data  

    def compress_data(self, binary_data, content_type):
      
        if content_type.startswith('image/'):
            return self.compress_image(binary_data, format='WEBP', quality=85)
        else:
            return zlib.compress(binary_data, level=9)

    def create(self, validated_data):
        user_images = validated_data.pop('user_images')
        nature = validated_data.get('nature', 'photos')

        user = validated_data['user']

        content_type = ContentType.objects.get_for_model(self.model_class)

        blobs_to_create = []
        for image_index, user_image in enumerate(user_images):
            binary_data = user_image.read()

            file_content_type = user_image.content_type

            compressed_data = self.compress_data(binary_data, file_content_type)

            blobs_to_create.append(
                UBlob(
                    content_type=content_type,
                    object_id=user.pk,
                    blob=compressed_data,  
                    nature=nature,  
                )
            )

        # Bulk create UBlob instances for performance
        return UBlob.objects.bulk_create(blobs_to_create)

    # def to_representation(self, instance):
    #     return {
    #         'blob_id': instance.blob_id,
    #         'user_id': instance.object_id,
    #         'nature': instance.nature,
    #     }
    
class UserBlobSerializer(serializers.Serializer):
    # blob_id = serializers.IntegerField()
    # object_id = serializers.IntegerField()
    # content_type_id = serializers.IntegerField()
    # nature = serializers.CharField()
    blob = serializers.SerializerMethodField()

    def decompress_data(self, compressed_data, content_type):
       
        if content_type.startswith('image/'):
            # Decompress images using Pillow
            try:
                image = Image.open(BytesIO(compressed_data))
                output = BytesIO()
                image.save(output, format=image.format)  # Save in the original format
                return output.getvalue()
            except Exception as e:
                print(f"Image decompression failed: {e}")
                return compressed_data  # Return original data if decompression fails
        else:
            # Decompress non-image data using zlib
            try:
                return zlib.decompress(compressed_data)
            except zlib.error as e:
                print(f"Decompression failed: {e}")
                return compressed_data  # Return original data if decompression fails

    def get_blob(self, instance):
            if instance.nature == 'photo' or instance.nature == 'identity':
                print("decompressed data is ", instance.nature)
                decompressed_data = self.decompress_data(instance.blob, "image/")
                return decompressed_data
            

class CarCreateBlobSerializer(serializers.Serializer):
    car_images = serializers.ListField(
        child=serializers.FileField(),  # Use FileField for binary files
        write_only=True
    )
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    nature = serializers.CharField(default='photos')

    def compress_image(self, binary_data, format='WEBP', quality=85):
        try:
            image = Image.open(BytesIO(binary_data))
            output = BytesIO()
            image.save(output, format=format, quality=quality)  
            return output.getvalue()
        except Exception as e:
            print(f"Image compression failed: {e}")
            return binary_data  

    def compress_data(self, binary_data, content_type):
        if content_type.startswith('image/'):
            return self.compress_image(binary_data, format='WEBP', quality=85)
        else:
            return zlib.compress(binary_data, level=9)

    def create(self, validated_data):
        car_images = validated_data.pop('car_images')
        nature = validated_data.get('nature', 'photos')

        car = validated_data['car']  # Directly using the Car instance

        blobs_to_create = []
        for image_index, car_image in enumerate(car_images):
            binary_data = car_image.read()

            file_content_type = car_image.content_type

            compressed_data = self.compress_data(binary_data, file_content_type)

            blobs_to_create.append(
                CBlob(
                    car=car,  # Direct foreign key relation to Car
                    nature=nature,  
                    blob=compressed_data,  
                )
            )

        # Bulk create CBlob instances for performance
        return CBlob.objects.bulk_create(blobs_to_create)
class CarBlobSerializer(serializers.Serializer):
    blob = serializers.SerializerMethodField()

    def decompress_data(self, compressed_data, content_type):
       
        if content_type.startswith('image/'):
            # Decompress images using Pillow
            try:
                image = Image.open(BytesIO(compressed_data))
                output = BytesIO()
                image.save(output, format=image.format)  # Save in the original format
                return output.getvalue()
            except Exception as e:
                print(f"Image decompression failed: {e}")
                return compressed_data  # Return original data if decompression fails
        else:
            # Decompress non-image data using zlib
            try:
                return zlib.decompress(compressed_data)
            except zlib.error as e:
                print(f"Decompression failed: {e}")
                return compressed_data  # Return original data if decompression fails

    def get_blob(self, instance):
        decompressed_data = self.decompress_data(instance.blob, "image/")  # Decompress image if nature matches
        return decompressed_data
