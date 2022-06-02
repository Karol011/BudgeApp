from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Item
        fields = '__all__'

class ReceiptSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Receipt
        fields = ['items']