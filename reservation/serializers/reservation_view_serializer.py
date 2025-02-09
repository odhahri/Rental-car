from rest_framework import serializers

from reservation.models import Reservation


class ReservationSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='reservation_id')
    reservation_client_key = serializers.IntegerField(source='client_id')
    reservation_car_key = serializers.IntegerField(source='car_id')
    reservation_start_date = serializers.DateTimeField(source='start_date')
    reservation_end_date = serializers.DateTimeField(source='end_date')
    reservation_status = serializers.CharField(source='status')
    reservation_processed_by = serializers.IntegerField(source='processedby_id')
    reservation_created_at = serializers.DateTimeField(source='created_at')
    reservation_updated_at = serializers.DateTimeField(source='updated_at')
