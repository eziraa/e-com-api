from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serialaizers import ProductSeriallizer


@api_view()
def ProductList(request):
    products = Product.objects.all()
    serializer = ProductSeriallizer(products, many=True)

    return Response(serializer.data)


@api_view()
def ProductDetail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSeriallizer(product)
    return Response(serializer.data)
