# Generated by Django 2.0.2 on 2018-04-23 16:41

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=255, null=True, verbose_name='姓名')),
                ('pass_word', models.CharField(max_length=255, verbose_name='密码')),
                ('id', models.CharField(max_length=255, primary_key=builtins.id, serialize=False, verbose_name='账号')),
            ],
            options={
                'db_table': 'T_XUPT_USER',
            },
        ),
    ]