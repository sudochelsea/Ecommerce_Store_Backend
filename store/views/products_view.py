from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.response import Response
from store.models.product_model import Product
from store.serializers.product_serializers import ProductSerializer
from django.http import Http404, HttpResponse, JsonResponse


# Create your views here.

class ProductsView(APIView):
    # getting all products from the database as JSON
    def get(self, request, format=None):

        product = Product.objects.filter(is_deleted=False)
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProductCreateView(APIView):

    def post(self, request, format=None):

        # this converts the JSON data into a python object
        # serializer acts as a translator
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get_objects(self, pk):
        try:
            return Product.objects.filter(id=pk, is_deleted=False)
        except Product.DoesNotExist:
            raise Http404('Not Found')


class ProductListView(APIView):
    def get(self, request, pk, format=None):
        product = self.get_objects(pk)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)


class ProductUpdateView(APIView):
    def put(self, request, pk, format=None):
        product = self.get_objects(pk)
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    def delete(self, request, pk, format=None):
        product = self.get_objects(pk)
        product.is_deleted = True

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
