# Generated by Django 4.0.3 on 2023-01-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0025_alter_user_address_city_alter_user_address_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_payment',
            name='admin_accept_status',
            field=models.TextField(choices=[('p', 'p'), ('a', 'a'), ('d', 'd')], default='p', max_length=1),
        ),
    ]
