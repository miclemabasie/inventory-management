# Generated by Django 3.0 on 2021-12-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_position_position_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='position_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]