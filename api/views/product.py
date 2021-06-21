from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from product.models import Product
from product.serializers import ProductSerializer


class ProductListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return Response()


class ProductDetailAPIView(APIView):

    def get_object(self):
        return Product.objects.get(slug=self.kwargs.get("slug"))

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_object()
            serializer = ProductSerializer(queryset, many=True, context={"request": request})
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

