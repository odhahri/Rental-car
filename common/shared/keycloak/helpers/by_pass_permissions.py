# import reverse
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse, resolve


class FilterByPassPermissions:
    @staticmethod
    def isGuest(request: WSGIRequest):
        kwargs = resolve(request.path_info).kwargs
        print(kwargs)
        if kwargs == {}:
            routes = {
                '/identification/signin/': 'POST',
                '/identification/signup/': 'POST',
                '/identification/connected-user/':'GET'
            }
            return routes.get(request.path) == request.method 
        # and not 'HTTP_AUTHORIZATION' in request.META


