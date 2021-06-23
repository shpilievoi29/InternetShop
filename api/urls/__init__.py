from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("product/", include("api.urls.product", namespace="product"), name="product"),
    path("user/", include("api.urls.user", namespace="user"), name="user"),
    path("order/", include("api.urls.order", namespace="order"), name="order"),
]
