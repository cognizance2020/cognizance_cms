# Generated by Django 3.1.4 on 2020-12-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_application_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='feedback',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='domain',
            field=models.CharField(choices=[('Cyber Security', 'Cyber Security'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Data Science', 'Data Science'), ('Competitive Programming', 'Competitive Programming'), ('Hackathons', 'Hackathons'), ('Open Source', 'Open Source')], max_length=100, null=True),
        ),
    ]
