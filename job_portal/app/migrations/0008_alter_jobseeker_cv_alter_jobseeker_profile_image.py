# Generated by Django 5.1.2 on 2024-11-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_jobpost_city_jobpost_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
