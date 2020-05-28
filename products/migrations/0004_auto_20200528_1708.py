# Generated by Django 3.0.6 on 2020-05-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200528_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Санат', 'verbose_name_plural': 'Санаттар'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Тапсырыс', 'verbose_name_plural': 'Тапсырыстар'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'өнім', 'verbose_name_plural': 'өнімдер'},
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=400, verbose_name='Мекен жайы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Аты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Багасы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='purchased_products',
            field=models.ManyToManyField(related_name='orders', to='products.Product', verbose_name='Тауарлар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category', verbose_name='Санаты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Сипаттама'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Сурет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Қолжетімділігі'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.TextField(verbose_name='Өндіруші'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Аты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Багасы'),
        ),
    ]
