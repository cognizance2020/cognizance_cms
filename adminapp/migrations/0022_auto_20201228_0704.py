# Generated by Django 3.1.4 on 2020-12-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0021_auto_20201223_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(null=True, upload_to='Achievements/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='Profile_Pics/'),
        ),
    ]