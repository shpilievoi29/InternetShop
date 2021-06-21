from rest_framework import serializers, request

from product.models import Category, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category"]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product:product_detail",
        lookup_field="slug",
    )
    url_api = serializers.HyperlinkedIdentityField(
        view_name="api:detail",
        lookup_field="slug",
    )
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
