# Generated by Django 3.0 on 2021-11-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20211125_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='positions',
            field=models.ManyToManyField(to='sales.Position'),
        ),
    ]
