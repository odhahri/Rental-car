from django.urls import path
from office.views import OfficeViewSet

urlpatterns = [
    path('', OfficeViewSet.as_view({'get': 'show_office_default_page'}), name='office_default_page'),
    path('cars/', OfficeViewSet.as_view({'get': 'show_office_cars_page'}), name='office_cars_page'),
    path('agents/', OfficeViewSet.as_view({'get': 'show_office_agents_page'}),name='office_agents_page'),
    path('reservations/', OfficeViewSet.as_view({'get': 'show_office_reservations_page'}), name='office_reservations_page'),
    path('clients/', OfficeViewSet.as_view({'get': 'show_office_clients_page'}),name='office_clients_page'),
    ]
