# Generated by Django 4.1 on 2022-09-01 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_chanel_owner_alter_chanel_reg_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanel',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 18, 17, 39, 117166, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 1, 18, 17, 39, 115883, tzinfo=datetime.timezone.utc)),
        ),
    ]
