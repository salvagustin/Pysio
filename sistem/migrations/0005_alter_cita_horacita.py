# Generated by Django 4.2.18 on 2025-02-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0004_cita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='horacita',
            field=models.CharField(blank=True, choices=[('1', '8:00 - 9:00'), ('2', '9:00 - 10:00'), ('3', '10:00 - 11:00'), ('4', '11:00 - 12:00'), ('5', '01:00 - 02:00'), ('6', '02:00 - 03:00'), ('7', '03:00 - 04:00'), ('8', '04:00 - 05:00'), ('9', '05:00 - 06:00')], max_length=1, null=True, verbose_name='Hora cita'),
        ),
    ]
