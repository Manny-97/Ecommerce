# Generated by Django 4.1 on 2022-08-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliveryoptions",
            name="delivery_name",
            field=models.CharField(
                help_text="Required", max_length=255, verbose_name="Delivery Name"
            ),
        ),
    ]
