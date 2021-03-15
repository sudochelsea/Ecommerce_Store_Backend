from django.urls import path
from store.views.products_view import ProductsView
from store.views.products_view import ProductView


app_name = 'store'
urlpatterns = [
        path('products/', ProductsView.as_view()),
        path('product/<int:pk>', ProductView.as_view()),
]