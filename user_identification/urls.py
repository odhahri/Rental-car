from django.urls import path
from user_identification.views import UserIdentificationViewSet
app_name = 'user_identification'
urlpatterns = [
    path('signin/', UserIdentificationViewSet.as_view({'post': 'signin'}),name='signin_user'),
    path('signup/', UserIdentificationViewSet.as_view({'post': 'signup'})),
    path('logout/', UserIdentificationViewSet.as_view({'get': 'logout'})),
    path('register/', UserIdentificationViewSet.as_view({'post': 'register_user'})),
    path('connected-user/',UserIdentificationViewSet.as_view({'get':'connected_user'})),
]
