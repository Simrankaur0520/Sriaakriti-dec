# Generated by Django 4.0.3 on 2023-01-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0020_alter_product_data_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_data',
            name='status',
            field=models.BooleanField(),
        ),
    ]
