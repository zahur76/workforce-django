# Generated by Django 3.2.8 on 2021-11-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pay_management", "0004_salaryslip_tax_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salaryslip",
            name="tax_number",
            field=models.IntegerField(),
        ),
    ]
