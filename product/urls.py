from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CurrencyViewSet, OrderViewSet

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('currency', CurrencyViewSet)
router.register('order', OrderViewSet)

app_name = 'product'
urlpatterns = [
    path('', include(router.urls)),
]

