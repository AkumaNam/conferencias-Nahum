# Generated by Django 3.2.3 on 2021-06-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0008_auto_20210616_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencia',
            name='duracion',
            field=models.SmallIntegerField(default='2'),
        ),
    ]
