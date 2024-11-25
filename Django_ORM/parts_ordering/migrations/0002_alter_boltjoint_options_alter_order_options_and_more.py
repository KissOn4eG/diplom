# Generated by Django 5.1.1 on 2024-09-09 20:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_ordering', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boltjoint',
            options={'verbose_name': 'болтовое соединение', 'verbose_name_plural': 'болтовые соединения'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'болтовое соединение', 'verbose_name_plural': 'болтовые соединения'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_list',
            new_name='order_items',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата и время создания заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.CharField(default='', max_length=250, verbose_name='заказчик'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]