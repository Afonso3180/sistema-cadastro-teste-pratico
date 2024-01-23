from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=200)
    suppliers = models.ManyToManyField('Supplier')
    price_history = models.ForeignKey('PriceHistory', on_delete=models.CASCADE, related_name = 'price_histories')
    reviews = models.ForeignKey('Review', on_delete=models.CASCADE, related_name = 'reviews')

class Supplier(models.Model):
    name = models.CharField(max_length=200)

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #n to 1
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #n to 1
    review = models.TextField()
    rating = models.IntegerField()