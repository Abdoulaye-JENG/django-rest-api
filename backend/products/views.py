from rest_framework import generics

from .serializers import ProductSerializer

from .models import Product


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"


class ProductCreateAPIView(generics.CreateAPIView):
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
