# Generated by Django 4.2 on 2023-05-01 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttb_backend', '0005_transaction_gift_bonus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholders_name', models.CharField(max_length=30)),
                ('card_number', models.IntegerField(validators=[django.core.validators.MinLengthValidator(13), django.core.validators.MaxLengthValidator(20)])),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(100)])),
                ('billing_address', models.CharField(max_length=100)),
            ],
        ),
    ]