from django.contrib import auth
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from django.db import models
from django.template.defaultfilters import slugify
from django.views.generic import RedirectView

import product
from product.validators import positive_validator
from django.core.validators import MaxValueValidator


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def __str__(self):
        return self.category

    @property
    def name(self):
        return self.category


class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    product = models.CharField(max_length=255, verbose_name=_("a product title"),
                               help_text=_("255 characters or fever"))
    amount = models.IntegerField(validators=[MaxValueValidator(1)], help_text=_("a positive "
                                                                                "integer"))
    product_description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='static/media/', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,
                                 db_column='category')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[positive_validator])
    slug = models.SlugField(max_length=255, help_text=_("letters, hyphens, numbers and"
                                                        " underscores"))

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product)
        if self.amount < 0:
            self.amount = 0

        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):

        return reverse_lazy("product:product_detail", kwargs={"slug": self.slug})

    @property
    def name(self):
        return self.product


class Review(models.Model):
    RATE_CHOICES = [
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]
    ]

    id = models.BigAutoField(primary_key=True)
    rate = models.PositiveSmallIntegerField(
        choices=RATE_CHOICES, default=5, verbose_name="product rate"
    )
    review = models.TextField(blank=True)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )

    class Meta:
        verbose_name = "product review"
        verbose_name_plural = "product reviews"

    def __repr__(self):
        return f"<Review ({self.id}) rate={self.rate}>"

    def __str__(self):
        return str(self.rate)


class Cart(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def get_total(self):
        total = 0.0
        for cart_item in self.cart_items:
            total + cart_item.get.total()

        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")

    def get_total(self):
        return Product.price * self.quantity


class Purchase(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
