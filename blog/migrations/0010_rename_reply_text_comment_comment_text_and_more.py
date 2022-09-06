# Generated by Django 4.1 on 2022-09-03 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_chanel_reg_date_alter_post_date_pub_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply_text',
            new_name='comment_text',
        ),
        migrations.AlterField(
            model_name='chanel',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 3, 30, 765779, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 3, 30, 768625, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 3, 30, 767075, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 3, 30, 764404, tzinfo=datetime.timezone.utc)),
        ),
    ]
