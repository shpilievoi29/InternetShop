from django.urls import path

from api.views.product import ProductListAPIView, ProductDetailAPIView

app_name = "product"

urlpatterns = [
    path('', ProductListAPIView.as_view(), name="list"),
    path('<slug:slug>/', ProductDetailAPIView.as_view(), name="detail"),
]
