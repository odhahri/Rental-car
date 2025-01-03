from django.urls import path
from reservation.views import ReservationViewSet

urlpatterns = [
    path('create/', ReservationViewSet.as_view({'post': 'create_reservation'})),
    path('list/', ReservationViewSet.as_view({'get': 'list_reservations'})),
    path('get/<int:pk>/', ReservationViewSet.as_view({'get': 'get_reservation'})),
    path('update/<int:pk>/', ReservationViewSet.as_view({'put': 'update_reservation'})),
    path('delete/<int:pk>/', ReservationViewSet.as_view({'delete': 'delete_reservation'})),
    # path('get_reservation_client/<int:pk>/', ReservationViewSet.as_view({'get': 'get_reservation_by_client'})),
]
