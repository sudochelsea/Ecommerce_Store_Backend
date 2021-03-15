from rest_framework import serializers
from store.models.category_model import Category


# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['product_name',]