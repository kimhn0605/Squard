# Generated by Django 3.1.4 on 2022-02-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_user_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_point',
            field=models.IntegerField(default=0, max_length=32, verbose_name='포인트'),
        ),
    ]
