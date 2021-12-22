# Generated by Django 3.0 on 2021-12-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20211204_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0.0, help_text='In XAF', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
