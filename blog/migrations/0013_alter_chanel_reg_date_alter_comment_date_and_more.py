# Generated by Django 4.1 on 2022-09-03 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_count_like_alter_chanel_reg_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanel',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 55, 44, 725905, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 55, 44, 728767, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 55, 44, 730128, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 55, 44, 727115, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 55, 44, 724589, tzinfo=datetime.timezone.utc)),
        ),
    ]
