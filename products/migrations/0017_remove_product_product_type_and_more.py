# Generated by Django 4.0.1 on 2022-01-18 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_rename_category_product_product_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='producttype',
            name='category',
        ),
    ]
