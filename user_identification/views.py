from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django.shortcuts import render

# rest framework django view 



class UserIdentificationViewSet(GenericViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    def signin(self, request):
        pass
    
    def signup(self, request):
        pass
    
    
    

     # HTML-based Views
    def signin_page(self, request):
        pass

    def signup_page(self, request, pk):
        pass