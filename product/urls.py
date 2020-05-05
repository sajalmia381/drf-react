from django.urls import path

from .views import *

app_name = 'product'
urlpatterns = [
    path('product/', product_list_via_api, name='product_list'),
    path('react-product', react_product_list, name='react_list'),

    # path('api/product', list_api_view, name="api_product_list"), # function base Serilizer
    path('api/product', ProductApiListView.as_view(), name="api_product_list"),
    path('api/product/create', api_product_create, name="api_product_create"),
]