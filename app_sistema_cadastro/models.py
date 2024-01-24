from django.db import models
import logging

logger = logging.getLogger(__name__)

class Supplier(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=200)
    suppliers = models.ManyToManyField('Supplier')
    
    def save(self, *args, **kwargs):
        logger.info(f'Salvando o produto {self.name}')
        super().save(*args, **kwargs)
    
class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'price_history') #n to 1
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'reviews') #n to 1
    review = models.TextField()
    rating = models.IntegerField()