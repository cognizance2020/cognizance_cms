# Generated by Django 3.1.4 on 2020-12-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0023_auto_20201228_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.CharField(max_length=250, null=True)),
                ('date', models.CharField(max_length=20, null=True)),
                ('time', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
