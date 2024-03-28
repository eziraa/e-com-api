from newsapi import NewsApiClient
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import ProductSerializer, CollectionSerializer


class ProductListView(APIView):
    def get(self, request):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class CollectionListView(APIView):
    def get(self, request):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)


class CollectionDetailView(APIView):
    def get(self, request, id):
        collection = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
