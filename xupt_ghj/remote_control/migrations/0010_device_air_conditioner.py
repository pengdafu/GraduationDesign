# Generated by Django 2.0.2 on 2018-05-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0009_auto_20180505_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='air_conditioner',
            field=models.IntegerField(null=True, verbose_name='是否是空调，0不是，1是'),
        ),
    ]