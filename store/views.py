from newsapi import NewsApiClient
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import AddressSerializer, CartSerializer, CategorySerializer, CustomerSerializer, DiscountSerializer, OrderItemSerializer, OrderSerializer, PaymentSerializer, ProductSerializer, CollectionSerializer, PromotionSerializer, ReviewSerializer, ShippingsSerializer, WishlistSerializer


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
        promotions = Promotion.objects.all()
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


class CartDetailView(APIView):
    def get(self, request, id):
        cart = get_object_or_404(Cart, pk=id)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class PaymentListView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class PaymentDetailsView(APIView):
    def get(self, request, id):
        payment = get_object_or_404(Payment, pk=id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class ReviewDetailsView(APIView):
    def get(self, request, id):
        review = get_object_or_404(Review, pk=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class WishListListView(APIView):
    def get(self, request):
        wishlists = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlists)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class WishListDetailsView(APIView):
    def get(self, request, id):
        wishlist = get_object_or_404(Wishlist, pk=id)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class DiscountListView(APIView):
    def get(self, request):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class DiscountDetailsView(APIView):
    def get(self, request, id):
        discount = get_object_or_404(Discount, pk=id)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class ShippingListView(APIView):
    def get(self, request):
        shippings = Shipping.objects.all()
        serializer = ShippingsSerializer(shippings)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class ShippingDetailsView(APIView):
    def get(self, request, id):
        shipping = get_object_or_404(Shipping, pk=id)
        serializer = ShippingsSerializer(shipping)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
