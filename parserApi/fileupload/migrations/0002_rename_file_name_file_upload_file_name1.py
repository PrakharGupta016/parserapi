# Generated by Django 3.2.15 on 2023-01-08 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file_upload',
            old_name='file_name',
            new_name='file_name1',
        ),
    ]
