# Generated by Django 4.1 on 2022-09-04 19:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_alter_chanel_reg_date_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanel',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 19, 9, 46, 965071, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 19, 9, 46, 967775, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 19, 9, 46, 969093, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 19, 9, 46, 966277, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 4, 19, 9, 46, 963672, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='UserRoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roots', models.CharField(max_length=100)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.chanel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_owner', to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel_worker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
