# Generated by Django 5.0.3 on 2024-04-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batirem', '0008_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
