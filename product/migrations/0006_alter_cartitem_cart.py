# Generated by Django 3.2.3 on 2021-06-09 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_cart_cartitem_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart'),
        ),
    ]
