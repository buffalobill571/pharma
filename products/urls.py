from django.urls import path
from .views import CategoryView, ProductListView, OrderCreateView
from rest_framework import routers

app_name = 'products'

router = routers.DefaultRouter()
router.register('products', ProductListView, basename='product')
router.register('categories', CategoryView, basename='category')

urlpatterns = [
    path('purchase/', OrderCreateView.as_view()),
] + router.urls
