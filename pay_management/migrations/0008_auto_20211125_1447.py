# Generated by Django 3.2.8 on 2021-11-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pay_management", "0007_alter_salaryslip_total_deduction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salaryslip",
            name="non_taxable_additional_allowances",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="salaryslip",
            name="taxable_additional_allowances",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
