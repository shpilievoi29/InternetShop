from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from order.models import Order
from order.serializers import OrderSerializer


class OrderListAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "id"
    lookup_field = "id"
