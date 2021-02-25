from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product, Currency, Order
from .serializers import ProductSerializer, CurrencySerializer, OrderSerializer
from utils.permission import IsNormalUser
from django.db.models import Sum


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    """
    class that manage all functionality of Product api
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsNormalUser)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.all()
        else:
            return self.queryset.filter(quantity__gt=0)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=['GET'], detail=False, url_path='purchased-product')
    def get_purchased_product(self, request):
        products = Product.objects.filter(order__user=self.request.user).distinct().all()
        return Response(
            {
                "data": ProductSerializer(products, many=True).data
            }
        )


class CurrencyViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class OrderViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['GET'], detail=False, url_path='total-revenue')
    def get_total_revenue(self, request):
        order_count = Order.objects.all().count()
        total_revenue = Order.objects.aggregate(Sum('total'))
        return Response(
            {"data": {
                    "total": total_revenue['total__sum'], "count": order_count
                }
            }, status=status.HTTP_200_OK
        )
