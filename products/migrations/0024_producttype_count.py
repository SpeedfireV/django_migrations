# Generated by Django 4.0.1 on 2022-01-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_order_surname_alter_order_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
