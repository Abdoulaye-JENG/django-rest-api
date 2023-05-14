from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    # Get the request body (data sent by the client)
    # The request param here is an instange of django HttpRequest
    # and has nothing to do with "pythin requests"
    body = request.body  # byte string JSON data
    data = {}
    try:
        data = json.loads(body)  # JSON String -> Python dict
    except:
        pass
    data["params"] = request.GET
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    print(data)
    return JsonResponse(data)
