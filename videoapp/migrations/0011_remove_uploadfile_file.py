# Generated by Django 3.2 on 2021-06-02 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0010_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='file',
        ),
    ]
