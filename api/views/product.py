from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import Product
from product.serializers import ProductSerializer


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "slug"
    lookup_field = "slug"

