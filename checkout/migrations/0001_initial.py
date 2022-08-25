# Generated by Django 4.1 on 2022-08-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeliveryOptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "delivery_name",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        verbose_name="Delivery Nme",
                    ),
                ),
                (
                    "delivery_price",
                    models.DecimalField(
                        decimal_places=2,
                        error_messages={
                            "name": {
                                "max_length": "The price must be between 0 and 999.99"
                            }
                        },
                        help_text="Maximum of 999.99",
                        max_digits=5,
                        verbose_name="Delivery Price",
                    ),
                ),
                (
                    "delivery_methods",
                    models.CharField(
                        choices=[
                            ("IS", "In Store"),
                            ("HD", "Home Delivery"),
                            ("DD", "Digital Delivery"),
                        ],
                        help_text="Required",
                        max_length=255,
                        verbose_name="Delivery Method",
                    ),
                ),
                (
                    "delivery_window",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        verbose_name="Delivery Window",
                    ),
                ),
                (
                    "delivery_timeframe",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        verbose_name="Delivery Timeframe",
                    ),
                ),
                (
                    "order",
                    models.IntegerField(
                        help_text="Required", verbose_name="order list"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Delivery option",
                "verbose_name_plural": "Delivery options",
            },
        ),
        migrations.CreateModel(
            name="PaymentSelection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="name"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Payment selection",
                "verbose_name_plural": "Payment selections",
            },
        ),
    ]
