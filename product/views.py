from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.parsers import JSONParser

from django_filters import rest_framework as filters

from .models import Product
from .serializers import ProductSerializer


class ProductFilter(filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['is_active', 'create_at']


class ProductApiListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ProductFilter



@api_view(['GET'])
def list_api_view(request):
    obj_list = Product.objects.all()
    serializer = ProductSerializer(obj_list, many=True)
    return Response(serializer.data, status=200)
    # return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def api_product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save(cresate_by=request.user)
        serializer.save()
        return Response({}, status=201)
    return Response({}, status="400")


def product_list_via_api(request, *args, **kwargs):
    """
        Product list with product data come through by api
    """
    return render(request, 'product/product_list.html')

def react_product_list(request, *args, **kwargs):
    return render(request, 'base_react.html')