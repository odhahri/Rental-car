from django.urls import path
from cars.views import CarViewSet
app_name = 'cars'
urlpatterns = [
    path('create/', CarViewSet.as_view({'post': 'create_car'})),
    path('list/', CarViewSet.as_view({'get': 'list_cars'})),
    path('get/<int:pk>/', CarViewSet.as_view({'get': 'get_car'})),
    path('update/<int:pk>/', CarViewSet.as_view({'put': 'update_car'})),
    path('delete/<int:pk>/', CarViewSet.as_view({'delete': 'delete_car'}),name='delete_car'),
    path('get_by_name/<str:name>/', CarViewSet.as_view({'get': 'get_car_by_name'})),
    path('car_list/', CarViewSet.as_view({'get': 'car_list_page'}),name='car_list_page'),
    path('car_detail/<int:pk>/', CarViewSet.as_view({'get': 'car_detail_page'}),name='car_detail_page'),
]
