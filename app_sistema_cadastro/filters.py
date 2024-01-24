import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name = 'price', lookup_exor = 'gte')
    max_price = django_filters.NumberFilter(field_name = 'price', lookup_exor = 'lte')
    
    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'name', 'sku']