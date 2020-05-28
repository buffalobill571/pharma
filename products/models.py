from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    description = models.TextField()
    manufacturer = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.FileField(blank=True, null=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Feature(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')


class Order(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    purchased_products = models.ManyToManyField(Product, related_name='orders')

    price = models.PositiveIntegerField()
