# Generated by Django 3.2.3 on 2021-06-03 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
                ('product_description', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/static/')),
                ('price', models.FloatField(null=True)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rate', models.IntegerField(choices=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], default=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'ordering': ['product'],
            },
        ),
    ]
