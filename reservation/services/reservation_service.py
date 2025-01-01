
from reservation.models import Reservation
from reservation.serializers.reservation_create_serializer import ReservationCreateInputSerializer, ReservationCreateOutputSerializer 
from reservation.serializers.reservation_update_serializer import ReservationUpdateSerializer
from reservation.serializers.reservation_view_serializer import ReservationSerializer
class ReservationService():
    def create(self, request):
        serializer = ReservationCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        output_serializer = ReservationCreateOutputSerializer(reservation)
        return output_serializer.data
    
    
    def list(self):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return serializer.data
    
    def get(self,pk):
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(reservation)
        # serializer.is_valid(raise_exception=True)
        return serializer.data
    
    def update(self,request,pk):
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationCreateInputSerializer(instance=reservation,data=request.data)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        outputserializer = ReservationUpdateSerializer(reservation)
        # outputserializer.is_valid(raise_exception=True)
        return outputserializer.data
    
    def delete(self,pk):
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()

    def get_by_name(self,name):
        reservation = reservation.objects.get(name=name)
        serializer = ReservationSerializer(reservation)
        return serializer.validated_data
    
