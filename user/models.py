from django.contrib import auth
from django.core.exceptions import ValidationError
from django.db import models

from product.validators import positive_validator


class Cash(models.Model):
    pid = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=100_000.00,
                                 validators=[positive_validator])
    username = models.OneToOneField("auth.User", on_delete=models.CASCADE)
