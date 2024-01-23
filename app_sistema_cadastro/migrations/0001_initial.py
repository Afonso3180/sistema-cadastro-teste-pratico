# Generated by Django 5.0.1 on 2024-01-23 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sku', models.CharField(max_length=200)),
                ('price_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_histories', to='app_sistema_cadastro.pricehistory')),
            ],
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sistema_cadastro.product'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_sistema_cadastro.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app_sistema_cadastro.review'),
        ),
        migrations.AddField(
            model_name='product',
            name='suppliers',
            field=models.ManyToManyField(to='app_sistema_cadastro.supplier'),
        ),
    ]
