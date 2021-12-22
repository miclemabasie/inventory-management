# Generated by Django 3.0 on 2021-12-03 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_category_number_of_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(help_text='In XAF', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]