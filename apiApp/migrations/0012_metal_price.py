# Generated by Django 4.0.3 on 2023-01-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0011_diamond_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='metal_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platinum', models.TextField()),
                ('gold', models.TextField()),
                ('making_charges', models.TextField()),
            ],
        ),
    ]
