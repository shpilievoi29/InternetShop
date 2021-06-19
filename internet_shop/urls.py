
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls.product', namespace="api")),
    path('', include('order.urls', namespace="order")),
    path('', include('user.urls', namespace="user")),
    path('', include('product.urls', namespace="products")),

]
