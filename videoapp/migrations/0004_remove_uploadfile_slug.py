# Generated by Django 3.2 on 2021-05-31 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0003_auto_20210531_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='slug',
        ),
    ]
