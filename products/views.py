from rest_framework import views, generics, viewsets
from drf_yasg.utils import swagger_auto_schema
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from .models import Category, Product, Feature


def get_client_ip(django_request_object):
    try:
        x_forwarded_for = django_request_object.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = django_request_object.META.get('REMOTE_ADDR')
    except KeyError:
        ip = '0.0.0.0'
    return ip


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_fields = ('category',)


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
