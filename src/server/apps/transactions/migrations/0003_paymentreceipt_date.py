# Generated by Django 4.2.2 on 2023-06-23 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("transactions", "0002_rename_add_amount_paymentreceipt_addamount_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentreceipt",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата",
            ),
            preserve_default=False,
        ),
    ]
