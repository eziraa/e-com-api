from newsapi import NewsApiClient
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import AddressSerializer, CartSerializer, CategorySerializer, CustomerSerializer, OrderItemSerializer, OrderSerializer, ProductSerializer, CollectionSerializer, PromotionSerializer


class ProductListView(APIView):
    def get(self, request):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class CollectionListView(APIView):
    def get(self, request):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class CollectionDetailView(APIView):
    def get(self, request, id):
        collection = get_object_or_404(Collection, pk=id)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class PromotionListView(APIView):
    def get(self, request):
        collections = Promotion.objects.all()
        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class PromotionDetailView(APIView):
    def get(self, request, id):
        promotion = get_object_or_404(Promotion, pk=id)
        serializer = PromotionSerializer(promotion)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class CategoryDetailView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, pk=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class CustomerDetailView(APIView):
    def get(self, request, id):
        customer = get_object_or_404(Customer, pk=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class OrderDetailView(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, pk=id)
        serializer = CategorySerializer(order)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class OrderItemListView(APIView):
    def get(self, request):
        orderItems = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderItems, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class OrderItemDetailView(APIView):
    def get(self, request, id):
        order = get_object_or_404(OrderItem, pk=id)
        serializer = OrderItemSerializer(order)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class AddressListView(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class AddressDetailView(APIView):
    def get(self, request, id):
        address = get_object_or_404(Address, pk=id)
        serializer = AddressSerializer(address)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class CartListView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

