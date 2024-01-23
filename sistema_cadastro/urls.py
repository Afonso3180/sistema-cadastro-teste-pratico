from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter 
from app_sistema_cadastro.views import ProductViewSet, SupplierViewSet, PriceHistoryViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'price_histories', PriceHistoryViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls))
]
