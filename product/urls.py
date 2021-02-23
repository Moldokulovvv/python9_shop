from django.urls import path

from .views import HomePageView, ProductsListView, ProductDetailsVIew
# from .views import products_list,product_details

urlpatterns = [
    path('', HomePageView.as_view(), name='index-page'),
    path('products/<slug:category_slug>/', ProductsListView.as_view(), name='products-list'),
    path('products/details/<int:pk>/', ProductDetailsVIew.as_view(), name="product-details")

]


