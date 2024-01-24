from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import Product, Supplier, PriceHistory, Review
from .serializers import ProductSerializer, SupplierSerializer, PriceHistorySerializer, ReviewSerializer
from decimal import Decimal

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name='Product1', 
            description='This is a test product',
            price=Decimal('10.99'), 
            sku='sku1'
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Product1')
        self.assertEqual(self.product.description, 'This is a test product')
        self.assertEqual(self.product.price, Decimal('10.99'))
        self.assertEqual(self.product.sku, 'sku1')

class SupplierModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.supplier = Supplier.objects.create(name='Supplier1')

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.name, 'Supplier1')

class PriceHistoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(name='Product1', description='This is a test product', price=10.99, sku='sku1')
        cls.price_history = PriceHistory.objects.create(price=Decimal('10.99'), product=product)

    def test_price_history_creation(self):
        self.assertEqual(self.price_history.price, Decimal('10.99'))

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(name='Product1', description='This is a test product', price=10.99, sku='sku1')
        cls.review = Review.objects.create(product=product, review='This is a test review', rating=5)

    def test_review_creation(self):
        self.assertEqual(self.review.review, 'This is a test review')
        self.assertEqual(self.review.rating, 5)
