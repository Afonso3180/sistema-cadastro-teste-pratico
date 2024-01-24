from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Product, Supplier, PriceHistory, Review
from .serializers import ProductSerializer, SupplierSerializer, PriceHistorySerializer, ReviewSerializer
from .filters import ProductFilter
import logging
from .tasks import update_average_rating

logger = logging.getLogger(__name__)

class TenItemsPagination(PageNumberPagination):
    page_size = 10

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    
    def list(self, request, *args, **kwargs):
        logger.info('Iniciando a listagem de produtos')
        response = super().list(request, *args, **kwargs)
        logger.info('Finalizando a listagem de produtos')
        return response
    
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        review = serializer.save()
        update_average_rating.delay(review.product_id)
