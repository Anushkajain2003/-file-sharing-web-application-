# Generated by Django 4.2.5 on 2023-10-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_fileshare_receiver_alter_fileshare_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileshare',
            name='file',
            field=models.FileField(upload_to='sharedfiles'),
        ),
    ]
