from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Санат'
        verbose_name_plural = 'Санаттар'


class Product(models.Model):
    name = models.CharField('Аты', max_length=300)
    price = models.PositiveIntegerField('Багасы')
    description = models.TextField('Сипаттама')
    manufacturer = models.TextField('Өндіруші')
    is_available = models.BooleanField('Қолжетімділігі', default=True)
    image = models.FileField('Сурет', blank=True, null=True)
    discount = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Санаты')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'өнім'
        verbose_name_plural = 'өнімдер'


class Feature(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')


class Order(models.Model):
    name = models.CharField('Аты', max_length=200)
    address = models.CharField('Мекен жайы', max_length=400)
    email = models.EmailField('Почта')
    phone = models.CharField('Номер', max_length=100)

    purchased_products = models.ManyToManyField(Product, related_name='orders', verbose_name='Тауарлар')

    price = models.PositiveIntegerField('Багасы')

    class Meta:
        verbose_name = 'Тапсырыс'
        verbose_name_plural = 'Тапсырыстар'
