# Generated by Django 5.1.2 on 2024-11-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_message_notifications_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='cv',
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='cv/'),
        ),
    ]
