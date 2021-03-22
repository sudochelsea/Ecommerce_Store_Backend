from django.db import models
from .category_model import Category


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

