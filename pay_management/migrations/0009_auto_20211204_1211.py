# Generated by Django 3.2.9 on 2021-12-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pay_management", "0008_auto_20211125_1447"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salaryslip",
            name="non_taxable_additional_allowances",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="salaryslip",
            name="taxable_additional_allowances",
            field=models.IntegerField(default=0),
        ),
    ]
