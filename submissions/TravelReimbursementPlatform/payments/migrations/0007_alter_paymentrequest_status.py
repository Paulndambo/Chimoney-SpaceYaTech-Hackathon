# Generated by Django 4.1.7 on 2023-09-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0006_alter_paymentrequest_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentrequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("approved", "Approved"),
                    ("declined", "Declined"),
                ],
                default="pending",
                max_length=255,
            ),
        ),
    ]