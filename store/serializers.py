from rest_framework import serializers

class UserSerializers(serializers.Serializer):
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=254)


class ProductSerializers(serializers.Serializer):
    productname = serializers.CharField(max_length=200)
    price = serializers.CharField(max_digits=5,decimal_places=2)
    discount_price = serializers.FloatField(blank=True,null=True)
    description = serializers.TextField()
    image = serializers.CharField(max_length=5000, null=True, blank=True)


class OrderSerializers(serializers.Serializer):
    user = serializers.Serializer('user', null=True)
    quantity = serializers.Serializer(default=1)


class Category(serializers.Serializer):
    name = serializers.CharField(max_length=200)
