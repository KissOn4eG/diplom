# Generated by Django 5.1.1 on 2024-09-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_ordering', '0006_alter_order_cost_alter_order_order_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(related_name='order_boltjoint', to='parts_ordering.boltjoint', verbose_name='состав заказа'),
        ),
    ]