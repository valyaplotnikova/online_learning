# Generated by Django 5.1.1 on 2024-10-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payments_amount_alter_payments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата оплаты'),
        ),
    ]
