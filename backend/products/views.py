from rest_framework import generics

from .serializers import ProductSerializer

from .models import Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Override the create method"""
        # serializer.save(self.request.user)
        validated_data = serializer.validated_data
        title = validated_data.get("title")
        content = validated_data.get("content") or None

        if content is None:
            content = title
        serializer.save(content=content)


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    """We want to perform the following actions:
    1. Handle List Products and Product Detail (ListView & DetailView)
       -> GET method
    2. Handle Create Product (Create View) -> POST method
    """
    if request.method == "GET":  # ListView|DetailView
        # We have to check if
        # we have to get a single product  (pk != None)
        # or a list of products (pk = None)
        if pk is not None:  # DetailView
            object = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(object, many=False).data
        else:  # ListView
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if request.method == "POST":  # CreateView
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)
