# Generated by Django 3.1.4 on 2020-12-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20201219_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='reviewer',
            field=models.CharField(choices=[('Sanjay', 'Sanjay'), ('Naresh Kumar', 'Naresh Kumar')], max_length=200, null=True),
        ),
    ]