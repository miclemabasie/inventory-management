# Generated by Django 3.0 on 2021-11-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20211115_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]