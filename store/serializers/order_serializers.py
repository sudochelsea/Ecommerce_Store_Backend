from rest_framework import serializers
from store.models.order_model import Order


class OrderSerializer(serializers.ModelSerializer):
     class Meta:
         model = Order
         fields = ['user','quantity']

