from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title',
                  'unit_price', 'collection', 'inventory', 'price_with_tax')
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax',

    )

    def calculate_tax(self, product: Product):
        return (product.unit_price.__float__() * 0.01).__round__(3)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return serializers.ValidationError("Confirm password must be the same as the password")


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'featured_product')
