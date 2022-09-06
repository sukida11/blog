# Generated by Django 4.1 on 2022-09-03 14:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_alter_chanel_reg_date_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chanel',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 42, 37, 726449, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 42, 37, 729190, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 42, 37, 730663, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 42, 37, 727667, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 14, 42, 37, 725161, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='UserLiked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
