from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # Serializer class that will help us (through the API)
    # return any product instance data
    # In serialized json data

    # We can enrich our ProductSerializer as well
    # by adding extra data
    s_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "title", "content", "sale_price", "s_discount"]

    def get_s_discount(self, instance):
        return instance.get_discount()
