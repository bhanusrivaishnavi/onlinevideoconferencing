# Generated by Django 3.2 on 2021-05-31 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0004_remove_uploadfile_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfile',
            options={},
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d/', verbose_name=''),
        ),
    ]
