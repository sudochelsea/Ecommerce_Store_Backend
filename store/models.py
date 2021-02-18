from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey('user', null = True, on_delete=models.CASCADE )
    quantity = models.IntegerField(default=1)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.quantity


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
