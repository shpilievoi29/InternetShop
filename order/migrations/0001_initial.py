# Generated by Django 3.2.3 on 2021-06-03 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_date', models.DateField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[[1, 'created'], [2, 'in process'], [3, 'complete']], default=1)),
                ('updated_date', models.DateField(auto_now=True)),
                ('address', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='product.product')),
            ],
        ),
    ]
