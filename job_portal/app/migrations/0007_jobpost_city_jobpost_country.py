# Generated by Django 5.1.2 on 2024-11-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_jobpost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='city',
            field=models.CharField(default='Karachi', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='country',
            field=models.CharField(default='Pakistan', max_length=200),
            preserve_default=False,
        ),
    ]
