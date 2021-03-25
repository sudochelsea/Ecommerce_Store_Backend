from rest_framework import serializers
from store.models.product_model import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = Product
         fields = ['pk','product_name','price','discount_price','description','image','category',]

