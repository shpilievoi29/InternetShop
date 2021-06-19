from django.urls import path, include

app_name = "api"

url_patterns = [
    path("", include("api.urls.product", namespace="product"), name="product"),
]
