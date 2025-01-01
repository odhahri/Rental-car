from django.urls import path
from cars.views import CarViewSet

urlpatterns = [
    path('create/', CarViewSet.as_view({'post': 'create_car'})),
    path('list/', CarViewSet.as_view({'get': 'list_cars'})),
    path('get/<int:pk>/', CarViewSet.as_view({'get': 'get_car'})),
    path('update/<int:pk>/', CarViewSet.as_view({'put': 'update_car'})),
    path('delete/<int:pk>/', CarViewSet.as_view({'delete': 'delete_car'})),
    path('get_by_name/<str:name>/', CarViewSet.as_view({'get': 'get_car_by_name'})),
    
]