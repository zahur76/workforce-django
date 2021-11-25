# Generated by Django 3.2.8 on 2021-11-25 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_management', '0002_alter_salaryslip_json_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salaryslip',
            name='tax_deduction',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
