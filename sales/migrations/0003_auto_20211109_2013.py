# Generated by Django 3.0 on 2021-11-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20211109_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
