from celery import shared_task
from .models import Product, Review
import logging

logger = logging.getLogger(__name__)

@shared_task
def update_average_rating(product_id):
    logger.info(f'Iniciando a atualização da avaliação média do produto {product_id}')
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product)
    average_rating = sum(review.rating for review in reviews) / reviews.count()
    product.average_rating = average_rating
    product.save()
    logger.info(f'Finalizando a atualização da avaliação média do produto {product_id}')
