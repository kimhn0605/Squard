# Generated by Django 3.1.4 on 2022-02-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_user_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_point',
            field=models.IntegerField(default=0, verbose_name='포인트'),
        ),
    ]