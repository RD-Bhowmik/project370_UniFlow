# Generated by Django 5.0.4 on 2024-04-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPUniflow', '0006_donor_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
