# Generated by Django 3.2.8 on 2021-11-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0007_remove_sickleave_sick_reset"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff",
            name="tax_number",
            field=models.IntegerField(default=99999),
        ),
    ]
