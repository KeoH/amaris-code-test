# Generated by Django 2.0.1 on 2018-01-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_auto_20180107_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('1', 'ET::BOSS'), ('2', 'ET::TECNIC'), ('3', 'ET::STUDENT')], default='2', max_length=2, verbose_name='FI::ROLE'),
        ),
    ]
