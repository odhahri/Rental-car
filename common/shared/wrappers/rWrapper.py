
from django.http import JsonResponse

def ResponseWrapper(data,message,success,status):
    response_data = {
        "data": data,
        "message": message,
        "success": success,
        "status": status
    }
    return JsonResponse(response_data, status=status)