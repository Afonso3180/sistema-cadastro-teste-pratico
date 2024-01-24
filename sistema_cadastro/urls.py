from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter 
from app_sistema_cadastro.views import ProductViewSet, SupplierViewSet, PriceHistoryViewSet, ReviewViewSet
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'price_histories', PriceHistoryViewSet)
router.register(r'reviews', ReviewViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API Docs",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls))
]
