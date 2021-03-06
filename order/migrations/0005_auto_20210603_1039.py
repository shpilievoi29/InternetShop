# Generated by Django 3.2.3 on 2021-06-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[[1, 'Created'], [2, 'Canceled'], [3, 'Confirmed'], [4, 'Completed'], [5, 'Rejected']], default=1),
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
    ]
