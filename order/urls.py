from django.urls import path
from django.views.generic import DeleteView

from order.views import OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView, \
    OrderDeleteView

app_name = "order"
urlpatterns = [
    path("order/", OrderListView.as_view(), name="order-list"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("<int:pk>/update/", OrderUpdateView.as_view(), name="order-update"),
    path("<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
]