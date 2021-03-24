from django.urls import path
from store.views.products_view import ProductListView
from store.views.products_view import ProductCreateView
from store.views.products_view import ProductDeleteView
from store.views.products_view import ProductDetailView
from store.views.products_view import ProductUpdateView


app_name = 'store'
urlpatterns = [
        path('products/', ProductListView.as_view()),
        path('create_product/', ProductCreateView.as_view()),
        path('delete_product/<int:pk>/', ProductDeleteView.as_view()),
        path('detail_product/<int:pk>/', ProductDetailView.as_view()),
        path('update_product/<int:pk>/', ProductUpdateView.as_view())
        # path('product/<int:pk>', ProductView.as_view()),
]