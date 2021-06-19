from django.urls import path

from api.views.product import ProductListAPIView

app_name = "product"

urlpatterns = [
    path('', ProductListAPIView.as_view(), name="list"),
]
