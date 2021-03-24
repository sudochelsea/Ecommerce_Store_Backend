from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from store.models.product_model import Product
from store.serializers.product_serializers import ProductSerializer
from django.http import Http404, HttpResponse, JsonResponse


# Create your views here.
# '''
# Helper method to get the object with given product_id
# '''

class ProductListView(APIView):
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


class ProductDetailView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk, is_deleted=False)
        except Product.DoesNotExist:
            raise Http404('Not Found')

    def get(self, request, pk, format=None):
        product = self.get_object(pk)

        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)


class ProductUpdateView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk, is_deleted=False)
        except Product.DoesNotExist:
            raise Http404('Not Found')

    def post(self, request, pk, format=None):
        product = self.get_object(pk)
        # we update the instance of the product instead of creating a new one
        serializer = ProductSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk, is_deleted=False)
        except Product.DoesNotExist:
            raise Http404('Not Found')

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.is_deleted = False

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
