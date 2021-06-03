from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    product = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    product_description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to='static/static/', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,
                                 db_column='category')
    price = models.FloatField(null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.product

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product)
        if self.amount < 0:
            self.amount = 0

        super(Product, self).save(*args, **kwargs)


class Review(models.Model):
    RATE_CHOICES = [
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]
    ]
    id = models.BigAutoField(primary_key=True)
    rate = models.IntegerField(choices=RATE_CHOICES, default=5)
    review = models.TextField
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        ordering = ["product"]

