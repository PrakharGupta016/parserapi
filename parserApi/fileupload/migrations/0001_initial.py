# Generated by Django 3.2.15 on 2023-01-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='file_upload',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
    ]
