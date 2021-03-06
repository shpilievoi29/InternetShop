from django.contrib import admin

from product.models import Product, Category, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category']
    ordering = ['id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['image', 'category', 'product', 'price', 'product_description', 'amount', 'slug']
    list_display = ['id', 'image', 'product', 'price', 'category', 'amount', 'product_description']
    ordering = ['id']
    prepopulated_fields = {'slug': ['product', ]}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields = ['id', 'product_id', "review", 'rate']
    list_display = ['id', 'product_id', "review", 'rate']
    ordering = ['id']
