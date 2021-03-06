# Generated by Django 3.2.7 on 2021-10-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="staff",
            options={"verbose_name_plural": "Staff"},
        ),
        migrations.AddField(
            model_name="staff",
            name="address",
            field=models.CharField(default=777, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="staff",
            name="phone_number",
            field=models.IntegerField(default=777, max_length=7),
            preserve_default=False,
        ),
    ]
