# Generated by Django 4.0.1 on 2022-01-16 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_orderposition_products_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='item_name',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='availability',
            old_name='item_count',
            new_name='products_count',
        ),
        migrations.RenameField(
            model_name='orderposition',
            old_name='order_number',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='order_number',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='orderposition',
            name='products_cost',
        ),
        migrations.AddField(
            model_name='orderposition',
            name='availability',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.availability'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderposition',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
