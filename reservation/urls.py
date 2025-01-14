from django.urls import path
from reservation.views import ReservationViewSet
app_name = 'reservations'
urlpatterns = [
    path('create/', ReservationViewSet.as_view({'post': 'create_reservation'}), name='add_reservation'),
    path('list/', ReservationViewSet.as_view({'get': 'list_reservations'})),
    path('get/<int:pk>/', ReservationViewSet.as_view({'get': 'get_reservation'})),
    path('update/<int:pk>/', ReservationViewSet.as_view({'put': 'update_reservation'}), name='update_reservation'),
    path('delete/<int:pk>/', ReservationViewSet.as_view({'delete': 'delete_reservation'}), name='delete_reservation'),
    # path('get_reservation_client/<int:pk>/', ReservationViewSet.as_view({'get': 'get_reservation_by_client'})),
]
