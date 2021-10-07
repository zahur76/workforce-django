# Generated by Django 3.2.7 on 2021-10-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email_address', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('management_level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=26)),
                ('entry_date', models.DateField()),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('position_held', models.CharField(max_length=254)),
                ('basic_salary', models.IntegerField()),
                ('transport_allowance', models.IntegerField()),
                ('annual_leave', models.IntegerField()),
                ('annual_leave_remaining', models.IntegerField()),
                ('sick_leave', models.IntegerField()),
                ('sick_leave_remaining', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
