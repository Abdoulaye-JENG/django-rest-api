from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):
    # Get the request body (data sent by the client)
    # The request param here is an instange of django HttpRequest
    # and has nothing to do with "pythin requests"
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
    return JsonResponse(data)
