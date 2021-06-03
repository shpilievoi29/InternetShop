from django import forms

from product.models import Product
from order.models import Order
from django.contrib.auth.models import User


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
