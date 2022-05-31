from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

class ReceiptSerializer(serializers.Serializer):
    item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Receipt
        fields = ['items']