from django.urls import path
from client.views import ClientViewSet

app_name = 'clients'
urlpatterns = [
    path('create/', ClientViewSet.as_view({'post': 'create_client'}),name='add_client'),
    path('list/', ClientViewSet.as_view({'get': 'list_clients'})),
    path('get/<int:pk>/', ClientViewSet.as_view({'get': 'get_client'})),
    path('update/<int:pk>/', ClientViewSet.as_view({'put': 'update_client'}),name='update_client'),
    path('delete/<int:pk>/', ClientViewSet.as_view({'delete': 'delete_client'}), name='delete_client'),
    path('get_by_name/<str:name>/', ClientViewSet.as_view({'get': 'get_client_by_name'})),

]
