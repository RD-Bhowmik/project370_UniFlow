# Generated by Django 5.0.4 on 2024-04-23 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APPUniflow', '0002_remove_doner_user_doner_username_alter_doner_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doner',
        ),
    ]
