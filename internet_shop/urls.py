
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace="api")),
    path('api-auth-token/', obtain_auth_token, name="auth-token"),
    path('', include('order.urls', namespace="order")),
    path('', include('user.urls', namespace="user")),
    path('', include('product.urls', namespace="products")),

]
