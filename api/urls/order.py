from django.urls import path

from api.views.order import OrderListAPIView, OrderDetailAPIView

app_name = "order"

urlpatterns = [
    path('', OrderListAPIView.as_view(), name="list"),
    path('<int:id>/', OrderDetailAPIView.as_view(), name="detail"),
]
