# Generated by Django 3.1.4 on 2020-12-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_member_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=1000, null=True)),
                ('achievers', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('date', models.DateField(null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
