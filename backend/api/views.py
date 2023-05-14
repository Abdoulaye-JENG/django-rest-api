# from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # Get the request body (data sent by the client)
    # The request param here is an instange of django HttpRequest
    # and has nothing to do with "python requests"q
    product_instance = Product.objects.all().order_by("?").first()
    data = {}
    if product_instance:
        # data = model_to_dict(instance)
        # We will use a serialisez instance instance
        serialized_product_instance = ProductSerializer(product_instance)
        data = serialized_product_instance.data
    return Response(data)
