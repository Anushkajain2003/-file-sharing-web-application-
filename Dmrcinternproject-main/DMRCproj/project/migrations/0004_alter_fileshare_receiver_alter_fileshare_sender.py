# Generated by Django 4.2.5 on 2023-10-10 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_fileshare_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileshare',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fileshare',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files_sent', to=settings.AUTH_USER_MODEL),
        ),
    ]