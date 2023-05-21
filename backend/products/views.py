from rest_framework import authentication, generics, mixins, permissions

from .serializers import ProductSerializer

from .models import Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

PRODUCT_SERIALIZER_QUERYSET = Product.objects.all()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = PRODUCT_SERIALIZER_QUERYSET
    serializer_class = ProductSerializer
    # lookup_field = "pk"


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = PRODUCT_SERIALIZER_QUERYSET
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    # Only Authenticated user can acces this view
    permission_classes = [permissions.IsAuthenticated]
    # Creation available only for authenticated users
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Override the create method"""
        # serializer.save(self.request.user)
        validated_data = serializer.validated_data
        title = validated_data.get("title")
        content = validated_data.get("content") or None

        if content is None:
            content = title
        serializer.save(content=content)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = PRODUCT_SERIALIZER_QUERYSET
    lookup_field = "pk"

    def perform_update(self, serializer):
        # Overriding this method makes sense only
        # if we have further operation to do with
        # The object instance (serializer)
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = PRODUCT_SERIALIZER_QUERYSET
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # Overriding this method like I dot it right below
        # has actually no sense because it is the default
        # operation
        super().perform_destroy(instance)


class ProductMixinView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = ProductSerializer
    queryset = PRODUCT_SERIALIZER_QUERYSET
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  # HTTP -> GET
        # List | Detail
        pk = kwargs.get("pk", None)
        if pk is not None:  # Detail
            return self.retrieve(request, *args, **kwargs)
        else:  # List
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # HTTP -> POST
        # Create
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):  # HTTP -> PUT
        # Update
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):  # HTTP -> DELETE
        # Destroy
        return self.destroy(request, *args, **kwargs)


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
