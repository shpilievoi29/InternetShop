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
