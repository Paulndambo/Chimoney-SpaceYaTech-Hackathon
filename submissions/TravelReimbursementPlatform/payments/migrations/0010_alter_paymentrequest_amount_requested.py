# Generated by Django 4.1.7 on 2023-09-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0009_alter_paymentrequest_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentrequest",
            name="amount_requested",
            field=models.IntegerField(default=0),
        ),
    ]