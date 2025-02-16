# Generated by Django 3.2 on 2022-02-04 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("parking_permits", "0013_refund_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parkingpermit",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="permits",
                to="parking_permits.customer",
                verbose_name="Customer",
            ),
        ),
    ]
