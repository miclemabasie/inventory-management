# Generated by Django 3.0 on 2021-12-05 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_auto_20211205_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='custormer',
            new_name='customer',
        ),
    ]