# Generated by Django 3.0 on 2021-11-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_purchase_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
    ]
