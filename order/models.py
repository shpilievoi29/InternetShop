import datetime
from datetime import timezone

from django.contrib import auth
from django.db import models
from django.urls import reverse_lazy

from product.models import Product


class Order(models.Model):
    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"

    id = models.BigAutoField(primary_key=True)

    CREATED = 1
    CANCELED = 2
    CONFIRMED = 3
    COMPLETED = 4
    REJECTED = 5

    ORDER_STATUSES = [
        [CREATED, "Created"],
        [CANCELED, "Canceled"],
        [CONFIRMED, "Confirmed"],
        [COMPLETED, "Completed"],
        [REJECTED, "Rejected"],
    ]
    status = models.IntegerField(choices=ORDER_STATUSES, default=1)
    created_date = models.DateField(auto_created=True, auto_now=True)
    updated_date = models.DateField(auto_now=True)
    address = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="+"
    )

    def __repr__(self):
        return f"Order ('{self.id}')"

    def __str__(self):
        return f"{self.id}|-product: {self.product}|-status: {self.status}|-address: {self.address}" \
               f"|-quantity:  {self.quantity}"

    def get_absolute_url(self):
        return reverse_lazy("order:order-detail", kwargs={"pk": self.id})
