# Generated by Django 3.2.3 on 2021-06-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateField(auto_created=True),
        ),
    ]
