from rest_framework import views, generics, viewsets
from drf_yasg.utils import swagger_auto_schema
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from .models import Category, Product, Feature
from rest_framework import filters


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


class CategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.query_params.get('search'):
            queryset = queryset.filter(name__istartswith=self.request.query_params.get('search').capitalize())
        if self.request.query_params.get('category'):
            queryset = queryset.filter(category_id=self.request.query_params.get('category'))
        return queryset


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
