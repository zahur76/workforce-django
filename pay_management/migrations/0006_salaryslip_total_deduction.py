# Generated by Django 3.2.8 on 2021-11-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_management', '0005_alter_salaryslip_tax_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='salaryslip',
            name='total_deduction',
            field=models.IntegerField(default=100),
        ),
    ]
