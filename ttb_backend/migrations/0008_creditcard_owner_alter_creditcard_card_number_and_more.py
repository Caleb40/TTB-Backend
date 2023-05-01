# Generated by Django 4.2 on 2023-05-01 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ttb_backend', '0007_alter_creditcard_card_number_alter_creditcard_cvv'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.CharField(max_length=4),
        ),
    ]
