# Generated by Django 3.1.4 on 2020-12-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_auto_20201208_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.CharField(choices=[('administrator', 'administrator'), ('member', 'member')], max_length=200, null=True),
        ),
    ]