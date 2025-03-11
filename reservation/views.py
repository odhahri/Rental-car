from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from common.shared.keycloak.constants import keycloak_scopes_resources
from reservation.services.reservation_service import ReservationService

# rest framework django view 

from .models import Reservation

class ReservationViewSet(GenericViewSet):
    keycloak_resources_scopes = keycloak_scopes_resources.keycloak_scopes_resources['reservation']

    queryset = Reservation.objects.all()
    reservation_service = ReservationService()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def create_reservation(self, request):
        reservation = self.reservation_service.create(request)
        return Response(data=reservation, status=201)
    
    def list_reservations(self, request):
        reservations = self.reservation_service.list()
        return Response(data=reservations, status=200)
    
    def get_reservation(self, request, pk):
        reservation = self.reservation_service.get(pk)
        return Response(data=reservation, status=200)
    
    def update_reservation(self, request, pk):
        reservation = self.reservation_service.update(request, pk)
        return Response(data='updated successfuly ! ', status=200)
    

    def delete_reservation(self, request, pk):
        self.reservation_service.delete(pk)
        return Response(status=204)
    
    def get_reservation_by_client(self, request, pk):
        reservation = self.reservation_service.get_by_client(pk)
        return Response(data=reservation, status=200)
    


