# Generated by Django 2.0.1 on 2018-01-07 18:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_employee_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='traveling_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, verbose_name='FI::TRAVELING_DATA'),
        ),
    ]
