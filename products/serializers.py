from rest_framework import serializers
from .models import Feature, Product, Category, Order


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'key', 'value')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'manufacturer', 'description', 'is_available', 'image', 'description', 'features')


class OrderSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=True)
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all(), write_only=True)
    purchased_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'address', 'email', 'products', 'price', 'phone', 'purchased_products')

    def create(self, validated_data):
        products = validated_data.pop('products')
        validated_data['price'] = sum([p.price for p in products])
        obj = super().create(validated_data)
        for p in products:
            obj.purchased_products.add(p)
        obj.save()
        return obj
