# from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from django.utils.translation import gettext_lazy as _


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


from rest_framework.authtoken.serializers import (
    AuthTokenSerializer as DRFAuthTokenSerializer,
)
from rest_framework.authtoken.views import ObtainAuthToken as DRFObtainAuthToken

from rest_framework import serializers
from django.contrib.auth import authenticate


class AuthTokenSerializer(DRFAuthTokenSerializer):
    username = None
    email = serializers.EmailField(label=_("Email"), write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                username=email,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class ObtainAuthToken(DRFObtainAuthToken):
    serializer_class = AuthTokenSerializer
