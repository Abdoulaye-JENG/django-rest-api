# from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home_v1(request, *args, **kwargs):
    # Get the request body (data sent by the client)
    # The request param here is an instance of django HttpRequest
    # and has nothing to do with "python requests"
    product_instance = Product.objects.all().order_by("?").first()
    data = {}
    if product_instance:
        # data = model_to_dict(instance)
        # We will use a serialize instance
        serialized_product_instance = ProductSerializer(product_instance)
        data = serialized_product_instance.data
    return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # Validate Post data according to the "ProductSerializer"
        # And the model (Product here) associated to the serialier itself

        # Here We can Save the data itself and get a product
        # instance (serialized) which will represent the
        # response

        # serializer = serializer.save()

        print("Serializer data:")
        print(serializer.data)
        return Response(serializer.data)
