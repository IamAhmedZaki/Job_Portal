# Generated by Django 5.1.1 on 2024-11-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_jobpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='status',
            field=models.CharField(default='enable', max_length=20),
            preserve_default=False,
        ),
    ]
