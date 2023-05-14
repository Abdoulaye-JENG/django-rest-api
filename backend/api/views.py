from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # Get the request body (data sent by the client)
    # The request param here is an instange of django HttpRequest
    # and has nothing to do with "python requests"
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)

    return Response(data)
