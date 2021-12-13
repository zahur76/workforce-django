# Generated by Django 3.2.7 on 2021-10-12 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0004_sickleave_days"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnnualLeave",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("days", models.IntegerField()),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annuallleave",
                        to="staff.staff",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Annual leave",
            },
        ),
    ]
