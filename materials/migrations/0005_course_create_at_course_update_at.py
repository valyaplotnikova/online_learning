# Generated by Django 5.1.1 on 2024-10-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время обновления курса'),
        ),
    ]
