# Generated by Django 5.0.1 on 2024-01-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prices',
            field=models.FloatField(),
        ),
    ]