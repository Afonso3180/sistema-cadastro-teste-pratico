from rest_framework import serializers
from .models import Product, Supplier, PriceHistory, Review

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name']

class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ['id', 'product', 'price', 'date']
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'review', 'rating']

class ProductSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many = True, read_only = True)
    price_history = PriceHistorySerializer(many = True, read_only = True)
    reviews = ReviewSerializer(many = True, read_only = True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'sku', 'suppliers', 'price_history', 'reviews']
