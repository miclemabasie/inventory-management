# Generated by Django 3.0 on 2021-11-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211115_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
