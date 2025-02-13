from django.urls import path
from cars.views import CarViewSet
app_name = 'cars'
urlpatterns = [
    path('create/', CarViewSet.as_view({'post': 'create_car'}),name='add_car'),
    path('list/', CarViewSet.as_view({'get': 'list_cars'})),
    path('get/<int:pk>/', CarViewSet.as_view({'get': 'get_car'})),
    path('update/<int:pk>/', CarViewSet.as_view({'put': 'update_car'}),name='update_car'),
    path('delete/<int:pk>/', CarViewSet.as_view({'delete': 'delete_car'}),name='delete_car'),
    path('get_by_name/<str:name>/', CarViewSet.as_view({'get': 'get_car_by_name'})),
    path('car_list/', CarViewSet.as_view({'get': 'car_list_page'}),name='car_list_page'),
    path('car_detail/<int:pk>/', CarViewSet.as_view({'get': 'car_detail_page'}),name='car_detail_page'),
    path('add_blobs_by_id/<int:pk>/', CarViewSet.as_view({'post': 'add_blobs_by_id'}),name='add_blobs_by_id'),
    path('get_blobs_by_id_and_nature/<int:pk>/<str:nature>', CarViewSet.as_view({'get': 'get_blobs_by_id'}),name='get_blobs_by_id'),
    path('list_car_with_availability/<int:pk>', CarViewSet.as_view({'get': 'list_car_with_availability'}),name='list_car_with_availability'),
]
