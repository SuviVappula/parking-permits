# Generated by Django 3.2 on 2021-11-11 08:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("parking_permits_app", "0030_vehicle_low_emission_vehicle"),
    ]

    operations = [
        migrations.CreateModel(
            name="Refund",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Time created"
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="Time modified"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=6,
                        verbose_name="Amount",
                    ),
                ),
                ("iban", models.CharField(max_length=30)),
                ("request_date", models.DateField(verbose_name="Start date")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPEN", "OPEN"),
                            ("IN_PROGRESS", "IN_PROGRESS"),
                            ("ACCEPTED", "ACCEPTED"),
                        ],
                        default="OPEN",
                        max_length=32,
                        verbose_name="Status",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="parking_permits_app.customer",
                        verbose_name="Customer",
                    ),
                ),
                (
                    "permit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="refunds",
                        to="parking_permits_app.parkingpermit",
                        verbose_name="Permit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Refund",
                "verbose_name_plural": "Refunds",
                "db_table": "refund",
            },
        ),
    ]
