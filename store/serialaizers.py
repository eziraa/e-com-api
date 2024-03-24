from rest_framework import serializers


class ProductSeriallizer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
