# Generated by Django 3.0 on 2021-11-24 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_remove_customer_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='about',
            field=models.TextField(null=True),
        ),
    ]
