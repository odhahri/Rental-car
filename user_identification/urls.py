from django.urls import path
from user_identification.views import UserIdentificationViewSet
app_name = 'user_identification'
urlpatterns = [
    path('identification_page/', UserIdentificationViewSet.as_view({'get': 'identification_page'}),name='identification_page'),
    path('signin_page/', UserIdentificationViewSet.as_view({'get': 'signin_page'}),name='signin_page'),
    path('signup_page/', UserIdentificationViewSet.as_view({'get': 'signup_page'})),
    
    path('signin/', UserIdentificationViewSet.as_view({'post': 'signin'}),name='signin_user'),
    path('signup/', UserIdentificationViewSet.as_view({'post': 'signup'})),
    
]
