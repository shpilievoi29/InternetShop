from django.urls import path

from product.views import ProductListView, ReviewCreateView,  ProductDetailView, AddToCartView,\
    PurchaseView

app_name = "product"
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("review/", ReviewCreateView.as_view(), name="review"),
    path("add-to-cart/<slug:slug>/", AddToCartView.as_view(), name="add-to-cart"),
    path("purchase/", PurchaseView.as_view(), name="purchase"),
]