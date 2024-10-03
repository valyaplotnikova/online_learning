# Generated by Django 5.1.1 on 2024-10-03 11:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_payments_amount_payments_link_to_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='amount',
            field=models.PositiveIntegerField(default=100, verbose_name='сумма оплаты'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
