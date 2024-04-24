# Generated by Django 5.0.4 on 2024-04-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPUniflow', '0011_bloodrequest_status_alter_bloodrequest_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodrequest',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='disease',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='need_within_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]